"""
Patches mkdocs-with-pdf for headless Chrome rendering with Mermaid.
Run after `pip install -r requirements.txt`.
"""
import re
import sys
from pathlib import Path


def find_package_path(package_name: str) -> Path | None:
    for p in sys.path:
        candidate = Path(p) / package_name
        if candidate.is_dir():
            return candidate
    # Fallback: try site-packages
    import site
    for sp in site.getsitepackages():
        candidate = Path(sp) / package_name
        if candidate.is_dir():
            return candidate
    return None


def patch_generator(pkg_path: Path) -> bool:
    file = pkg_path / 'generator.py'
    if not file.exists():
        print(f"  NOT FOUND: {file}")
        return False

    content = file.read_text(encoding='utf-8')
    changes = 0

    # 1. Fix tag.text → tag.string (BeautifulSoup compat)
    old = "                    tag.text = self._mixed_script"
    new = "                    tag.string = self._mixed_script"
    if old in content:
        content = content.replace(old, new)
        changes += 1
        print("  + Patched tag.text → tag.string")
    else:
        print("  - tag.text not found (already patched?)")

    # 2. Inject Mermaid CDN script before theme scripts
    marker = "        scripts = self._theme.get_script_sources()"
    mermaid_injection = """\
        body = soup.find('body')
        if body:
            # Pre-load Mermaid for Chrome headless rendering (PDF)
            mermaid_script = soup.new_tag(
                'script', src='https://unpkg.com/mermaid@11/dist/mermaid.min.js')
            body.insert(0, mermaid_script)

        scripts = self._theme.get_script_sources()"""
    if marker in content and 'mermaid_script' not in content:
        content = content.replace(marker, mermaid_injection)
        changes += 1
        print("  + Injected Mermaid CDN script loader")
    elif 'mermaid_script' in content:
        print("  - Mermaid injection already present")
    else:
        print(f"  WARNING: marker '{marker}' not found")
        return False

    file.write_text(content, encoding='utf-8')
    print(f"  → {file} updated ({changes} change(s))")
    return True


def patch_headless_chrome(pkg_path: Path) -> bool:
    file = pkg_path / 'drivers' / 'headless_chrome.py'
    if not file.exists():
        print(f"  NOT FOUND: {file}")
        # Try alternative location (flat structure)
        file = pkg_path / 'headless_chrome.py'
        if not file.exists():
            return False

    content = file.read_text(encoding='utf-8')
    old = "'--virtual-time-budget=10000'"
    new = "'--virtual-time-budget=30000'"
    if old in content:
        content = content.replace(old, new)
        file.write_text(content, encoding='utf-8')
        print(f"  + Increased virtual-time-budget: 10s → 30s")
        return True
    else:
        print("  - virtual-time-budget already patched or different")
        return False


def main():
    pkg_path = find_package_path('mkdocs_with_pdf')
    if not pkg_path:
        print("ERROR: mkdocs-with-pdf not found in site-packages")
        sys.exit(1)

    print(f"Found mkdocs-with-pdf at: {pkg_path}")
    ok = True

    print("\nPatching generator.py ...")
    ok &= patch_generator(pkg_path)

    print("\nPatching headless Chrome driver ...")
    patch_headless_chrome(pkg_path)

    if ok:
        print("\n✅ All patches applied successfully")
    else:
        print("\n❌ Some patches failed")
        sys.exit(1)


if __name__ == '__main__':
    main()
