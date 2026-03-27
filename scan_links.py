import os
import re
from urllib.parse import urlparse

base_dir = r"c:\Users\USER\geinei_clean"
broken_links = []

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            hrefs = re.findall(r'href=[\"\']([^\"\']+)[\"\']', content)
            srcs = re.findall(r'src=[\"\']([^\"\']+)[\"\']', content)
            
            for link in hrefs + srcs:
                if link.startswith('http') or link.startswith('mailto:') or link.startswith('tel:') or link.startswith('#') or link.startswith('data:'):
                    continue
                
                parsed = urlparse(link)
                clean_link = parsed.path
                if not clean_link: continue
                
                if clean_link.startswith('/'):
                    target_path = os.path.join(base_dir, clean_link.lstrip('/'))
                else:
                    target_path = os.path.normpath(os.path.join(root, clean_link))
                
                if not os.path.exists(target_path):
                    broken_links.append(f"{f} -> {link}")

if broken_links:
    print('Found broken links:')
    for b in set(broken_links):
        print(b)
else:
    print('No broken links found.')
