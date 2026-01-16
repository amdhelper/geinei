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
    
    original_content = content
    
    # Find the top bar (hidden-mobile div with #002FA7 background) and add z-index
    # Pattern: class="hidden-mobile" style="background:#002FA7;..." or similar
    # We need to add position:relative;z-index:200 to this div
    
    # Pattern 1: background-color: #002FA7 (with spaces)
    content = re.sub(
        r'(class="hidden-mobile"[^>]*style="[^"]*background-color:\s*#002FA7[^"]*)"',
        lambda m: add_zindex_to_style(m.group(0)),
        content
    )
    
    # Pattern 2: background:#002FA7 (without spaces)
    content = re.sub(
        r'(class="hidden-mobile"[^>]*style="[^"]*background:\s*#002FA7[^"]*)"',
        lambda m: add_zindex_to_style(m.group(0)),
        content
    )
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Updated: {filepath}")
        return True
    else:
        print(f"  No changes: {filepath}")
        return False

def add_zindex_to_style(match_str):
    # Check if z-index already exists
    if 'z-index' in match_str:
        return match_str
    
    # Add position:relative;z-index:200 before the closing quote
    # The match ends with "
    if match_str.endswith('"'):
        # Remove trailing quote, add styles, put quote back
        return match_str[:-1] + ';position:relative;z-index:200"'
    return match_str

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    updated_count = 0
    
    print("Adding z-index to top bar...")
    
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
