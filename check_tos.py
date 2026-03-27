import os
import re

base_dir = r"c:\Users\USER\geinei_clean"

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            hrefs = re.findall(r'href=[\"\']([^\"\']+)[\"\']', content)
            for link in hrefs:
                if link in ('terms-of-service.html', 'privacy-policy.html'):
                    target_path = os.path.normpath(os.path.join(root, link))
                    if not os.path.exists(target_path):
                        print(f"Broken in {path} -> {link}")
