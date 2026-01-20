#!/usr/bin/env python3
"""
Fix product card heights across all language versions
"""
import os
import re

BASE_DIR = r"c:\Users\USER\geinei_clean"

def fix_product_cards_all(filepath):
    """Fix product card height consistency with flexible pattern matching"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already fixed (has flex-direction: column in premium-card)
        if 'premium-card' in content and 'flex-direction: column' in content:
            return False
        
        # Pattern to find .premium-card style block
        pattern = r'(\.premium-card\s*\{[^}]+height:\s*100%;?\s*\})'
        
        def replace_func(match):
            old_block = match.group(1)
            # Add flexbox properties
            if 'display: flex' not in old_block:
                new_block = old_block.replace(
                    'height: 100%;',
                    '''height: 100%;
            display: flex;
            flex-direction: column;'''
                ).replace(
                    'height:100%;',
                    '''height:100%;display:flex;flex-direction:column;'''
                )
                # Add child styles after the closing brace
                new_block += '''
        
        .premium-card > div:last-child {
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        
        .premium-card > div:last-child p {
            flex: 1;
        }'''
                return new_block
            return old_block
        
        new_content = re.sub(pattern, replace_func, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def fix_contact_title_all(filepath):
    """Fix contact title size on mobile for all languages"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has mobile title fix
        if 'font-size: 32px !important' in content or 'font-size:32px!important' in content:
            return False
        
        # Find @media(max-width:768px) block and add our fix
        # Look for the existing media query
        patterns = [
            r'(@media\s*\(\s*max-width\s*:\s*768px\s*\)\s*\{)\s*\n*\s*(\.hidden-mobile)',
            r'(@media\(max-width:768px\)\{)(\.hidden-mobile)'
        ]
        
        fix_css = '''
            /* Contact Title Mobile Fix */
            h1 {
                font-size: 32px !important;
            }
            
            section {
                padding: 50px 0 !important;
            }
            '''
        
        for pattern in patterns:
            if re.search(pattern, content):
                new_content = re.sub(pattern, r'\1' + fix_css + r'\2', content)
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    return True
        
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def find_all_html():
    """Find all relevant HTML files"""
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    print("=== Fixing Product Card Heights & Contact Title ===\n")
    
    html_files = find_all_html()
    products_fixed = 0
    contacts_fixed = 0
    
    for filepath in html_files:
        filename = os.path.basename(filepath)
        
        # Fix product pages
        if 'products.html' in filepath or 'applications.html' in filepath:
            if fix_product_cards_all(filepath):
                print(f"✓ Product cards: {filepath}")
                products_fixed += 1
        
        # Fix contact pages
        if 'contact.html' in filepath:
            if fix_contact_title_all(filepath):
                print(f"✓ Contact title: {filepath}")
                contacts_fixed += 1
    
    print(f"\nProducts fixed: {products_fixed}")
    print(f"Contacts fixed: {contacts_fixed}")

if __name__ == "__main__":
    main()
