import os
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.links = []
        self.images = []
        self.has_title = False
        self.has_desc = False
        self.in_title = False
        self.title_content = ""
        
    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == 'a' and 'href' in attr_dict:
            self.links.append(attr_dict['href'])
        elif tag == 'img':
            self.images.append(attr_dict)
        elif tag == 'title':
            self.in_title = True
        elif tag == 'meta' and attr_dict.get('name', '').lower() == 'description':
            if attr_dict.get('content', '').strip():
                self.has_desc = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
            if self.title_content.strip():
                self.has_title = True

    def handle_data(self, data):
        if self.in_title:
            self.title_content += data

def check_local_site(base_dir):
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        if '.git' in root or '.vscode' in root: continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
                
    problems = []
    
    # Check each file
    for filepath in html_files:
        rel_path = os.path.relpath(filepath, base_dir).replace('\\', '/')
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parser = MyHTMLParser(rel_path)
        try:
            parser.feed(content)
        except Exception as e:
            problems.append(f"[{rel_path}] Parse error: {e}")
            continue
            
        if not parser.has_title:
            problems.append(f"[{rel_path}] Missing or empty <title>")
        if not parser.has_desc:
            problems.append(f"[{rel_path}] Missing or empty meta description")
            
        for img in parser.images:
            if 'alt' not in img:
                problems.append(f"[{rel_path}] Image missing alt attribute: {img.get('src')}")
                
        # Basic link checking for internal html files
        for link in parser.links:
            # ignore external, mailto, tel, anchor
            if link.startswith('http') or link.startswith('mailto:') or link.startswith('tel:') or link.startswith('#'):
                continue
            
            clean_link = link.split('#')[0].split('?')[0]
            if not clean_link:
                continue
                
            if clean_link.endswith('.html') or clean_link.endswith('.pdf') or clean_link.endswith('.jpg') or clean_link.endswith('.png'):
                dir_path = os.path.dirname(filepath)
                if clean_link.startswith('/'):
                    target_path = os.path.join(base_dir, clean_link.lstrip('/'))
                else:
                    target_path = os.path.normpath(os.path.join(dir_path, clean_link))
                    
                if not os.path.exists(target_path):
                    problems.append(f"[{rel_path}] Broken internal link/asset: {link} (Expected at {target_path})")
                        
    out_path = os.path.join(base_dir, 'site_health_report.txt')
    with open(out_path, 'w', encoding='utf-8') as f:
        if problems:
            for p in problems:
                f.write(p + '\n')
        else:
            f.write("No major issues found.\n")
            
    print(f"Health check complete. Found {len(problems)} potential issues.")
    if len(problems) > 0:
        print("First 20 issues:")
        for p in problems[:20]:
            print(p)

if __name__ == '__main__':
    check_local_site(r'c:\Users\USER\geinei_clean')
