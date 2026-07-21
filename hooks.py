import hashlib
import os
import re
import subprocess
import tempfile
from pathlib import Path

PRERENDER = os.environ.get('PRERENDER_MERMAID', '0') == '1'
PUPPETEER_CONFIG = Path(__file__).parent / 'puppeteer-config.json'

_cache = {}


_current_page = ''


def _mmdc_render(code: str, mmd_path: str, png_path: str) -> bool:
    args = [
        'mmdc', '-i', mmd_path, '-o', png_path,
        '-b', 'transparent', '-s', '1',
    ]
    if PUPPETEER_CONFIG.exists():
        args.extend(['-p', str(PUPPETEER_CONFIG)])
    result = subprocess.run(args, capture_output=True, text=True, timeout=30)
    return result.returncode == 0


def _quote_labels(code: str) -> str:
    """Wrap unquoted labels in quotes to handle special characters."""
    def _wrap(m):
        inner = m.group(1)
        if inner.startswith('"') and inner.endswith('"'):
            return m.group(0)
        esc = inner.replace('\\', '\\\\').replace('"', '\\"')
        return f'["{esc}"]'
    return re.sub(r'\[([^\[\]]*)\]', _wrap, code)


def _render_mermaid_png(code: str, index: int) -> str | None:
    key = hashlib.sha256(code.encode()).hexdigest()
    if key in _cache:
        return _cache[key]

    result_png = b''

    def _attempt(mmd_text: str) -> bool:
        nonlocal result_png
        with tempfile.NamedTemporaryFile(suffix='.mmd', delete=False, mode='w') as f_in:
            f_in.write(mmd_text)
            mmd_path = f_in.name
        png_path = mmd_path.replace('.mmd', '.png')
        ok = _mmdc_render(mmd_text, mmd_path, png_path)
        if ok:
            result_png = Path(png_path).read_bytes()
        for p in [mmd_path, png_path]:
            Path(p).unlink(missing_ok=True)
        return ok

    strategies = [
        ('original', code),
        ('quoted labels', _quote_labels(code)),
    ]

    for name, text in strategies:
        try:
            if _attempt(text):
                import base64
                b64 = base64.b64encode(result_png).decode()
                data_uri = f'data:image/png;base64,{b64}'
                _cache[key] = data_uri
                return data_uri
        except Exception as e:
            print(f'  [hooks] mmdc {name} exception ({_current_page}, idx {index}): {e}')

    print(f'  [hooks] mmdc all strategies failed ({_current_page}, idx {index})')
    _cache[key] = None
    return None


MERMAID_RE = re.compile(
    r'<pre class="mermaid"[^>]*><code[^>]*>(.*?)</code></pre>',
    re.DOTALL,
)


def on_page_markdown(markdown, page, config, files):
    site_url = config.get('site_url', '').rstrip('/')
    return markdown.replace('{{ site_url }}', site_url)


def on_page_content(html, page, config, files):
    if not PRERENDER:
        return html

    _cache.clear()
    rendered = [0]
    global _current_page
    _current_page = page.url

    def _replace(match):
        code = match.group(1)
        code = code.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
        code = code.replace('&quot;', '"').replace('&#39;', "'")

        data_uri = _render_mermaid_png(code, rendered[0])
        rendered[0] += 1

        if data_uri:
            return f'<p><img class="mermaid-rendered" src="{data_uri}" alt="Mermaid diagram" style="max-width:70%;height:auto;max-height:350px;" /></p>'
        return match.group(0)

    result = MERMAID_RE.sub(_replace, html)

    if rendered[0] > 0:
        print(f'  [hooks] Pre-rendered {rendered[0]} Mermaid diagram(s) on {page.url}')

    return result
