import hashlib
import os
import posixpath
import re
import subprocess
import tempfile
from pathlib import Path

PRERENDER = os.environ.get('PRERENDER_MERMAID', '0') == '1'
PUPPETEER_CONFIG = Path(__file__).parent / 'puppeteer-config.json'

_cache = {}

_current_page = ''
_site_dir = ''


def _mermaid_asset_dir() -> Path:
    d = Path(_site_dir) / 'assets' / 'mermaid'
    d.mkdir(parents=True, exist_ok=True)
    return d


def _relative_asset_path(page_url: str, filename: str) -> str:
    """Path to the shared mermaid asset dir, relative to the current page."""
    page_dir = posixpath.dirname(page_url)
    target = posixpath.join('assets', 'mermaid', filename)
    if not page_dir:
        return target
    return posixpath.relpath(target, start=page_dir)


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
                filename = f'{key}.png'
                out_path = _mermaid_asset_dir() / filename
                if not out_path.exists():
                    out_path.write_bytes(result_png)
                rel_path = _relative_asset_path(_current_page, filename)
                _cache[key] = rel_path
                return rel_path
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
    global _current_page, _site_dir
    _current_page = page.url
    _site_dir = config['site_dir']

    def _replace(match):
        code = match.group(1)
        code = code.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
        code = code.replace('&quot;', '"').replace('&#39;', "'")

        rel_path = _render_mermaid_png(code, rendered[0])
        rendered[0] += 1

        if rel_path:
            return f'<p><img class="mermaid-rendered" src="{rel_path}" alt="Mermaid diagram" style="max-width:70%;height:auto;max-height:350px;" /></p>'
        return match.group(0)

    result = MERMAID_RE.sub(_replace, html)

    if rendered[0] > 0:
        print(f'  [hooks] Pre-rendered {rendered[0]} Mermaid diagram(s) on {page.url}')

    return result
