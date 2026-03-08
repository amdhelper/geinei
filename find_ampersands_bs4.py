import os
from bs4 import BeautifulSoup

def find_headings_with_ampersands(root_dir):
    results = []
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        soup = BeautifulSoup(f, 'html.parser')
                        for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                            for tag in soup.find_all(tag_name):
                                inner_html = str(tag.decode_contents())
                                # Check if tag contains & and NOT the span
                                if '&' in inner_html:
                                    # Check if it already has the span
                                    if 'font-family' not in inner_html or 'sans-serif' not in inner_html:
                                        results.append((path, tag_name, inner_html.strip()))
                except Exception as e:
                    print(f"Error reading {path}: {e}")
    return results

if __name__ == "__main__":
    root = r"c:\Users\USER\geinei_clean"
    findings = find_headings_with_ampersands(root)
    if not findings:
        print("No un-replaced ampersands in headings found.")
    for path, tag, content in findings:
        print(f"File: {path}")
        print(f"[{tag}]: {content}")
        print("-" * 20)
