import os
import re

BASE_URL = "https://yehsheng.com"

# language directories
LANGS = {
    "en": "", # root
    "de": "de",
    "jp": "jp",
    "zh": "zh",
    "zh-cn": "zh-cn"
}

HREFLANG_CODES = {
    "en": "en",
    "de": "de",
    "jp": "ja",
    "zh": "zh-Hant",
    "zh-cn": "zh-Hans"
}

def get_canonical_url(lang, filename):
    if filename == "index.html":
        return f"{BASE_URL}/" if lang == "en" else f"{BASE_URL}/{LANGS[lang]}/"
    return f"{BASE_URL}/{filename}" if lang == "en" else f"{BASE_URL}/{LANGS[lang]}/{filename}"

def fix_file(filepath, base_dir, filename, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # Generate new tags
    canonical_url = get_canonical_url(lang, filename)
    new_tags_lines = []
    new_tags_lines.append(f'    <link href="{canonical_url}" rel="canonical" />')
    new_tags_lines.append('    <!-- hreflang tags for multilingual SEO -->')
    
    for l, d in LANGS.items():
        # check if file exists in that language
        check_path = os.path.join(base_dir, d, filename) if d else os.path.join(base_dir, filename)
        if os.path.exists(check_path):
            url = get_canonical_url(l, filename)
            new_tags_lines.append(f'    <link href="{url}" hreflang="{HREFLANG_CODES[l]}" rel="alternate" />')
            if l == "en":
                new_tags_lines.append(f'    <link href="{url}" hreflang="x-default" rel="alternate" />')
                
    new_tags_str = '\n'.join(new_tags_lines) + '\n'
    
    # 1. Remove all existing canonical tags and hreflang tags
    # We use a pattern that matches the whole line if the tag is the only thing on the line, to avoid blank lines
    content = re.sub(r'^[ \t]*<link[^>]*rel=["\']canonical["\'][^>]*>\s*\n', '', content, flags=re.IGNORECASE | re.MULTILINE)
    content = re.sub(r'<link[^>]*rel=["\']canonical["\'][^>]*>', '', content, flags=re.IGNORECASE)
    
    content = re.sub(r'^[ \t]*<link[^>]*hreflang=[^>]*>\s*\n', '', content, flags=re.IGNORECASE | re.MULTILINE)
    content = re.sub(r'<link[^>]*hreflang=[^>]*>', '', content, flags=re.IGNORECASE)
    
    content = re.sub(r'^[ \t]*<!--\s*hreflang tags.*?\s*-->\s*\n', '', content, flags=re.IGNORECASE | re.MULTILINE)
    content = re.sub(r'<!--\s*hreflang tags.*?\s*-->', '', content, flags=re.IGNORECASE)
    
    # 2. Insert the new tags exactly before </head>
    # Find </head> and replace it
    if '</head>' in content:
        content = content.replace('</head>', new_tags_str + '</head>')
    elif '</HEAD>' in content:
        content = content.replace('</HEAD>', new_tags_str + '</HEAD>')
    else:
        print(f"  ⚠️ No </head> tag found in {filepath}!")
        return False
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = r"c:\Users\USER\geinei_clean"
    modified = 0
    parsed = 0
    
    for root, dirs, files in os.walk(base_dir):
        # skip hidden dirs etc
        if ".git" in root or ".vscode" in root or "assets" in root or "images" in root:
            continue
            
        for file in files:
            if file.endswith(".html") and file not in ["404.html", "test_bs4.html", "products.htm"]:
                filepath = os.path.join(root, file)
                rel_dir = os.path.relpath(root, base_dir)
                lang = "en"
                
                if rel_dir in ["de", "jp", "zh", "zh-cn"]:
                    lang = rel_dir
                elif rel_dir != ".":
                    continue # ignore subfolders that aren't languages
                
                parsed += 1
                if fix_file(filepath, base_dir, file, lang):
                    modified += 1
                    print(f"✅ Updated {rel_dir}/{file}")
                    
    print(f"\n{'='*50}")
    print(f"Total files parsed: {parsed}")
    print(f"Total files updated: {modified}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
