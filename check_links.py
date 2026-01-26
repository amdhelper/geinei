import os
import re
from pathlib import Path

def get_all_html_files(base_dir):
    return list(Path(base_dir).rglob("*.html"))

def find_links(content):
    # Find href="..." and src="..."
    hrefs = re.findall(r'href=["\'](.*?)["\']', content)
    srcs = re.findall(r'src=["\'](.*?)["\']', content)
    return hrefs + srcs

def check_link(base_dir, current_file_path, link):
    if link.startswith(("http", "https", "mailto:", "tel:", "#")):
        return True
    
    # Remove query string or hash
    link = link.split('?')[0].split('#')[0]
    if not link:
        return True

    if link.startswith("/"):
        full_path = Path(base_dir) / link.lstrip("/")
    else:
        full_path = (Path(current_file_path).parent / link).resolve()
    
    return full_path.exists()

def main():
    base_dir = "c:/Users/USER/geinei_clean"
    html_files = get_all_html_files(base_dir)
    
    broken_links = []
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            links = find_links(content)
            for link in links:
                if not check_link(base_dir, html_file, link):
                    broken_links.append((html_file, link))
    
    if broken_links:
        print(f"Found {len(broken_links)} broken links:")
        for file, link in broken_links:
            print(f"- {file}: {link}")
    else:
        print("No broken links found!")

if __name__ == "__main__":
    main()
