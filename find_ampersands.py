import os
import re

def find_headings_with_ampersands(root_dir):
    heading_re = re.compile(r'<(h[1-6])[^>]*>(.*?)</h\1>', re.IGNORECASE | re.DOTALL)
    amp_re = re.compile(r'&(amp;)?', re.IGNORECASE)
    span_re = re.compile(r'<span style="font-family: [\'"](Inter|Noto Sans JP|Noto Sans SC|Noto Sans TC|Arial)[\'"], sans-serif;">&amp;</span>')
    
    results = []
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        matches = heading_re.findall(content)
                        for tag, inner_html in matches:
                            if amp_re.search(inner_html):
                                if not span_re.search(inner_html):
                                    results.append((path, tag, inner_html.strip()))
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
