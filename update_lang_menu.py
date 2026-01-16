import os
import re

# Directories to update
DIRS = ['zh', 'zh-cn']

# HTML pages to update
PAGES = ['index.html', 'about.html', 'products.html', 'contact.html', 'solutions.html', 
         'capabilities.html', 'applications.html', 'resources.html', 'emerging-tech.html']

# Old language menu pattern (3 languages)
OLD_PATTERN_ZH = r'''<a href="../zh-cn/([^"]+)"
                        style="display:block;padding:10px 15px;color:#333;font-size:13px">简体中文</a>
                </div>'''

# New language menu with 5 languages
def get_new_menu(page_name, current_lang):
    zh_style = 'color:#C5A059;font-size:13px;background:#f5f5f5' if current_lang == 'zh' else 'color:#333;font-size:13px'
    zh_cn_style = 'color:#C5A059;font-size:13px;background:#f5f5f5' if current_lang == 'zh-cn' else 'color:#333;font-size:13px'
    
    return f'''<a href="../zh-cn/{page_name}" style="display:block;padding:10px 15px;color:#333;font-size:13px">简体中文</a>
                    <a href="../de/{page_name}" style="display:block;padding:10px 15px;color:#333;font-size:13px">Deutsch</a>
                    <a href="../jp/{page_name}" style="display:block;padding:10px 15px;color:#333;font-size:13px">日本語</a>
                </div>'''

def update_file(filepath, current_lang):
    page_name = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has German/Japanese
    if '../de/' in content and '../jp/' in content:
        print(f"  Already updated: {filepath}")
        return False
    
    # Find and replace the language menu
    # Pattern: after zh-cn link, add de and jp links
    old_part = f'''<a href="../zh-cn/{page_name}"
                        style="display:block;padding:10px 15px;color:#333;font-size:13px">简体中文</a>
                </div>'''
    
    new_part = f'''<a href="../zh-cn/{page_name}" style="display:block;padding:10px 15px;color:#333;font-size:13px">简体中文</a>
                    <a href="../de/{page_name}" style="display:block;padding:10px 15px;color:#333;font-size:13px">Deutsch</a>
                    <a href="../jp/{page_name}" style="display:block;padding:10px 15px;color:#333;font-size:13px">日本語</a>
                </div>'''
    
    if old_part in content:
        new_content = content.replace(old_part, new_part)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Updated: {filepath}")
        return True
    
    # Try alternative pattern
    old_part2 = f'''<a href="../zh-cn/{page_name}"
                        style="display:block;padding:10px 15px;color:#333;font-size:13px">簡體中文</a>
                </div>'''
    
    if old_part2 in content:
        new_part2 = f'''<a href="../zh-cn/{page_name}" style="display:block;padding:10px 15px;color:#333;font-size:13px">簡體中文</a>
                    <a href="../de/{page_name}" style="display:block;padding:10px 15px;color:#333;font-size:13px">Deutsch</a>
                    <a href="../jp/{page_name}" style="display:block;padding:10px 15px;color:#333;font-size:13px">日本語</a>
                </div>'''
        new_content = content.replace(old_part2, new_part2)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Updated: {filepath}")
        return True
    
    # Try more flexible pattern using regex
    pattern = r'(<a href="\.\./zh-cn/' + re.escape(page_name) + r'"[^>]*>(?:简体中文|簡體中文)</a>)\s*</div>'
    match = re.search(pattern, content)
    if match:
        replacement = match.group(1) + '''
                    <a href="../de/''' + page_name + '''" style="display:block;padding:10px 15px;color:#333;font-size:13px">Deutsch</a>
                    <a href="../jp/''' + page_name + '''" style="display:block;padding:10px 15px;color:#333;font-size:13px">日本語</a>
                </div>'''
        new_content = re.sub(pattern, replacement, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Updated (regex): {filepath}")
        return True
    
    print(f"  Pattern NOT found: {filepath}")
    return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    updated_count = 0
    
    for dir_name in DIRS:
        dir_path = os.path.join(base_dir, dir_name)
        print(f"\nProcessing {dir_name}/")
        
        if not os.path.exists(dir_path):
            print(f"  Directory not found: {dir_path}")
            continue
        
        for page in PAGES:
            filepath = os.path.join(dir_path, page)
            if os.path.exists(filepath):
                if update_file(filepath, dir_name):
                    updated_count += 1
            else:
                print(f"  File not found: {page}")
    
    print(f"\nTotal updated: {updated_count} files")

if __name__ == '__main__':
    main()
