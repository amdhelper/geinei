import os
import re

# English pages that need updating (in root directory)
PAGES = ['contact.html', 'products.html', 'solutions.html', 'capabilities.html', 
         'applications.html', 'resources.html', 'emerging-tech.html']

def update_file(filepath):
    page_name = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has German/Japanese links
    if f'de/{page_name}' in content and f'jp/{page_name}' in content:
        print(f"  Already updated: {page_name}")
        return False
    
    # Pattern: zh-cn link followed by closing div
    pattern = rf'(<a href="zh-cn/{re.escape(page_name)}"[^>]*>🇨🇳\s*简体中文</a>)\s*</div>'
    
    replacement = rf'''\1
                    <a href="de/{page_name}" style="display: block; padding: 12px 20px; color: #333; font-size: 14px; border-bottom: 1px solid #eee;">🇩🇪 Deutsch</a>
                    <a href="jp/{page_name}" style="display: block; padding: 12px 20px; color: #333; font-size: 14px;">🇯🇵 日本語</a>
                </div>'''
    
    new_content, count = re.subn(pattern, replacement, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Updated: {page_name}")
        return True
    
    # Try alternative: look for simpler pattern
    pattern2 = rf'(zh-cn/{re.escape(page_name)}"[^>]*>.*?简体中文</a>)\s*</div>'
    match = re.search(pattern2, content, re.DOTALL)
    if match:
        old_text = match.group(0)
        new_text = match.group(1) + f'''
                    <a href="de/{page_name}" style="display: block; padding: 12px 20px; color: #333; font-size: 14px; border-bottom: 1px solid #eee;">🇩🇪 Deutsch</a>
                    <a href="jp/{page_name}" style="display: block; padding: 12px 20px; color: #333; font-size: 14px;">🇯🇵 日本語</a>
                </div>'''
        new_content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Updated (alt): {page_name}")
        return True
    
    print(f"  Pattern not found: {page_name}")
    return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    updated_count = 0
    
    print("Updating English pages with German and Japanese links...")
    
    for page in PAGES:
        filepath = os.path.join(base_dir, page)
        if os.path.exists(filepath):
            if update_file(filepath):
                updated_count += 1
        else:
            print(f"  File not found: {page}")
    
    print(f"\nTotal updated: {updated_count} files")

if __name__ == '__main__':
    main()
