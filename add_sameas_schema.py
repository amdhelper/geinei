import os
import sys
import json
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath('.')

INDEX_FILES = [
    'index.html', 'zh/index.html', 'zh-cn/index.html', 'de/index.html', 'jp/index.html',
    'about.html', 'zh/about.html', 'zh-cn/about.html', 'de/about.html', 'jp/about.html',
    'contact.html', 'zh/contact.html', 'zh-cn/contact.html', 'de/contact.html', 'jp/contact.html'
]

updated_count = 0
for rel_path in INDEX_FILES:
    filepath = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    modified = False

    schemas = soup.find_all('script', type='application/ld+json')
    for s in schemas:
        if not s.string:
            continue
        try:
            data = json.loads(s.string)
            changed = False
            
            # Helper to update organization object
            def process_org(obj):
                nonlocal changed
                if isinstance(obj, dict):
                    types = obj.get('@type')
                    is_org = False
                    if isinstance(types, list) and 'Organization' in types:
                        is_org = True
                    elif types == 'Organization':
                        is_org = True
                    
                    if is_org:
                        same_as = obj.get('sameAs', [])
                        if not isinstance(same_as, list):
                            same_as = [same_as] if same_as else []
                        if "https://www.linkedin.com/company/142922152/" not in same_as:
                            same_as.append("https://www.linkedin.com/company/142922152/")
                            obj['sameAs'] = same_as
                            changed = True

            if isinstance(data, dict):
                if '@graph' in data:
                    for item in data['@graph']:
                        process_org(item)
                else:
                    process_org(data)

            if changed:
                new_string = json.dumps(data, ensure_ascii=False, indent=2)
                s.string = f"\n{new_string}\n"
                modified = True
        except Exception as e:
            print(f"Error parsing json in {rel_path}: {e}")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        updated_count += 1
        print(f"Added sameAs to Organization schema in {rel_path}")

print(f"Successfully updated sameAs field in {updated_count} files.")
