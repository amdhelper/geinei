#!/usr/bin/env python3
"""
Script to:
1. Add mobile menu close button to all pages
2. Fix German and Japanese resources pages to match English version structure
"""
import os
import re

BASE_DIR = r"c:\Users\USER\geinei_clean"

# Mobile menu close button HTML to insert after mobile menu opens
CLOSE_BUTTON_HTML = '''<!-- Close Button -->
                <div onclick="toggleMenu()" style="text-align:right;padding:5px 0 15px;cursor:pointer;font-size:24px;color:#333;">✕</div>'''

def add_mobile_close_button(filepath):
    """Add close button to mobile menu if not already present"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if close button already exists
        if '✕' in content and 'toggleMenu()' in content:
            return False
            
        # Find the mobile menu div and insert close button after it
        pattern = r'(<div class="mobile-menu" id="mobileMenu"[^>]*>)'
        replacement = r'\1\n' + CLOSE_BUTTON_HTML
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def find_all_html_files():
    """Find all HTML files in the project"""
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    print("=== Adding Mobile Menu Close Buttons ===")
    html_files = find_all_html_files()
    updated_count = 0
    
    for filepath in html_files:
        if add_mobile_close_button(filepath):
            print(f"✓ Updated: {filepath}")
            updated_count += 1
    
    print(f"\nTotal files updated with close button: {updated_count}")
    print("\n=== Note ===")
    print("German and Japanese resources pages need manual update to match English content.")
    print("Please review de/resources.html and jp/resources.html")

if __name__ == "__main__":
    main()
