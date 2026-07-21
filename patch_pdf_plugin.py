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

    # 2. Remove any previous Mermaid CDN injection (no longer needed - pre-rendered at build time)
    marker = "        scripts = self._theme.get_script_sources()"
    removal_patterns = [
        ("        body = soup.find('body')", marker),
    ]
    for start_marker, end_marker in removal_patterns:
        idx = content.find(start_marker)
        end_idx = content.find(end_marker, idx)
        if idx >= 0 and end_idx > idx and 'mermaid' in content[idx:end_idx]:
            old_block = content[idx:end_idx]
            content = content.replace(old_block, '')
            changes += 1
            print("  + Removed previous Mermaid CDN injection")

    # 3. Also remove fallback renderer if present
    fb_marker = '# Fallback Mermaid renderer'
    if fb_marker in content:
        fb_start = content.find(fb_marker)
        fb_end = content.find('\n\n        return self._options.js_renderer.render(str(soup))', fb_start)
        if fb_start >= 0 and fb_end > fb_start:
            content = content[:fb_start] + content[fb_end:]
            changes += 1
            print("  + Removed previous Mermaid fallback renderer")
    else:
        print("  - No Mermaid fallback renderer found (first run)")

    file.write_text(content, encoding='utf-8')
    print(f"  → {file} updated ({changes} change(s))")
    return True


def patch_headless_chrome(pkg_path: Path) -> bool:
    file = pkg_path / 'drivers' / 'headless_chrome.py'
    if not file.exists():
        print(f"  NOT FOUND: {file}")
        file = pkg_path / 'headless_chrome.py'
        if not file.exists():
            return False

    content = file.read_text(encoding='utf-8')
    changes = 0

    # Increase virtual time budget. CI runners are far slower/more constrained
    # than a local dev machine, so headless Chrome needs much more real time
    # to finish parsing/rendering the whole combined book before --dump-dom
    # is forced to snapshot whatever it has (silently truncating the PDF).
    for old_val in (
        "'--virtual-time-budget=10000'",
        "'--virtual-time-budget=30000'",
        "'--virtual-time-budget=60000'",
        "'--virtual-time-budget=120000'",
    ):
        if old_val in content:
            new_val = "'--virtual-time-budget=1200000'"
            if old_val == new_val:
                print("  - virtual-time-budget already at 1200s")
            else:
                old_budget = old_val.split('=')[-1].rstrip("'")
                content = content.replace(old_val, new_val)
                print(f"  + Increased virtual-time-budget: {old_budget} → 1200s")
                changes += 1
            break

    # Add extra flags for CI compatibility (dev/shm, extensions, networking)
    extra_flags = [
        "'--disable-dev-shm-usage',",
        "'--disable-extensions',",
        "'--disable-background-networking',",
    ]
    insert_after = "'--disable-web-security',\n                        '--allow-file-access-from-files'"
    replacement = "'--disable-web-security',\n                        '--disable-dev-shm-usage',\n                        '--disable-extensions',\n                        '--disable-background-networking',\n                        '--allow-file-access-from-files'"
    if all(f not in content for f in extra_flags):
        if insert_after in content:
            content = content.replace(insert_after, replacement)
            print("  + Added --disable-dev-shm-usage, --disable-extensions, --disable-background-networking")
            changes += 1
        else:
            print("  - WARNING: insertion anchor not found for extra flags")
    else:
        print("  - Extra flags already present")

    # Revert --headless=old back to --headless if present
    headless_old = "'--headless=old',"
    headless_new = "'--headless',"
    if headless_old in content:
        content = content.replace(headless_old, headless_new)
        print("  + Reverted --headless=old → --headless")
        changes += 1
    elif headless_new in content:
        print("  - --headless already set (not old mode)")

    file.write_text(content, encoding='utf-8')
    print(f"  → headless_chrome.py updated ({changes} change(s))")
    return True


def patch_en_dash(pkg_path: Path) -> bool:
    """Fix en-dash (U+2013) typo in Chrome flags."""
    files_to_check = [
        pkg_path / 'drivers' / 'headless_chrome.py',
    ]
    patched = False
    for file in files_to_check:
        if not file.exists():
            continue
        content = file.read_text(encoding='utf-8')
        if '\u2013' in content:
            content = content.replace('\u2013', '-')
            file.write_text(content, encoding='utf-8')
            print(f"  + Fixed en-dash (U+2013) → hyphen in {file.name}")
            patched = True
        else:
            print(f"  - No en-dash found in {file.name}")
    return patched


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

    print("\nFixing en-dash typo in Chrome flags ...")
    patch_en_dash(pkg_path)

    if ok:
        print("\n✅ All patches applied successfully")
    else:
        print("\n❌ Some patches failed")
        sys.exit(1)


if __name__ == '__main__':
    main()
