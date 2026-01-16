import os
import re

# All directories to update
DIRS = ['', 'zh', 'zh-cn', 'de', 'jp']  # '' is root

# HTML pages to update
PAGES = ['index.html', 'about.html', 'products.html', 'contact.html', 'solutions.html', 
         'capabilities.html', 'applications.html', 'resources.html', 'emerging-tech.html']

def update_file(filepath):
    page_name = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    new_content = content
    
    # Fix 1: Increase z-index of langMenu from 100 to 10000
    if 'id="langMenu"' in new_content or "id='langMenu'" in new_content:
        # Pattern for langMenu z-index:100
        new_content = re.sub(
            r'(id=["\']langMenu["\'][^>]*z-index:)\s*100\b',
            r'\g<1>10000',
            new_content
        )
        if new_content != content:
            modified = True
    
    # Fix 2: Increase z-index of langDropdown from 1000 to 10000
    if 'id="langDropdown"' in new_content or "id='langDropdown'" in new_content:
        new_content = re.sub(
            r'(id=["\']langDropdown["\'][^>]*z-index:)\s*1000\b',
            r'\g<1>10000',
            new_content
        )
        if new_content != content:
            modified = True
    
    # Fix 3: Also ensure the parent top-bar has higher z-index than nav
    # The top-bar containing the language selector needs a z-index
    # Add z-index to the top bar div if not present
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Updated: {filepath}")
        return True
    else:
        print(f"  No changes: {filepath}")
        return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    updated_count = 0
    
    print("Updating z-index for language dropdowns...")
    
    for dir_name in DIRS:
        if dir_name:
            dir_path = os.path.join(base_dir, dir_name)
            print(f"\nProcessing {dir_name}/")
        else:
            dir_path = base_dir
            print(f"\nProcessing root/")
        
        if not os.path.exists(dir_path):
            print(f"  Directory not found")
            continue
        
        for page in PAGES:
            filepath = os.path.join(dir_path, page)
            if os.path.exists(filepath):
                if update_file(filepath):
                    updated_count += 1
            else:
                print(f"  File not found: {page}")
    
    print(f"\nTotal updated: {updated_count} files")

if __name__ == '__main__':
    main()
