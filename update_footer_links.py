#!/usr/bin/env python3
"""
Script to update footer links across all HTML files.
Updates Privacy Policy and Terms of Service links from '#' to actual page paths.
"""

import os
import re
from pathlib import Path

def update_footer_links(file_path: str, is_subdirectory: bool = False) -> bool:
    """
    Update footer links in an HTML file.
    
    Args:
        file_path: Path to the HTML file
        is_subdirectory: If True, use relative paths (../) for links
    
    Returns:
        True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Determine the correct prefix for links
        prefix = "../" if is_subdirectory else ""
        
        # Define all language variations
        privacy_texts = [
            'Privacy Policy',           # English
            '隱私權政策',                 # Traditional Chinese
            '隐私政策',                   # Simplified Chinese  
            'Datenschutz',              # German
            'プライバシーポリシー',        # Japanese
        ]
        
        terms_texts = [
            'Terms of Service',          # English
            '服務條款',                    # Traditional Chinese
            '服务条款',                    # Simplified Chinese
            'Nutzungsbedingungen',       # German
            '利用規約',                    # Japanese
        ]
        
        # Update Privacy Policy links
        for text in privacy_texts:
            # Match href="#" with various spacing
            pattern = rf'<a\s+href="#"\s+style="color:\s*#667;\s*font-size:\s*13px;">{re.escape(text)}</a>'
            replacement = f'<a href="{prefix}privacy-policy.html" style="color: #667; font-size: 13px;">{text}</a>'
            content = re.sub(pattern, replacement, content)
        
        # Update Terms of Service links
        for text in terms_texts:
            pattern = rf'<a\s+href="#"\s+style="color:\s*#667;\s*font-size:\s*13px;">{re.escape(text)}</a>'
            replacement = f'<a href="{prefix}terms-of-service.html" style="color: #667; font-size: 13px;">{text}</a>'
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    base_dir = Path(__file__).parent
    
    # Root level HTML files
    root_files = [
        'index.html', 'products.html', 'solutions.html', 'capabilities.html',
        'applications.html', 'about.html', 'contact.html', 'resources.html',
        'emerging-tech.html', '404.html'
    ]
    
    # Subdirectories with translations
    subdirs = ['zh', 'zh-cn', 'de', 'jp']
    
    modified_count = 0
    
    # Update root level files
    print("Updating root level HTML files...")
    for filename in root_files:
        filepath = base_dir / filename
        if filepath.exists():
            if update_footer_links(str(filepath), is_subdirectory=False):
                print(f"  ✓ Updated: {filename}")
                modified_count += 1
            else:
                print(f"  - No changes: {filename}")
        else:
            print(f"  ⚠ Not found: {filename}")
    
    # Update subdirectory files
    for subdir in subdirs:
        subdir_path = base_dir / subdir
        if subdir_path.exists() and subdir_path.is_dir():
            print(f"\nUpdating {subdir}/ directory...")
            for html_file in subdir_path.glob('*.html'):
                if update_footer_links(str(html_file), is_subdirectory=True):
                    print(f"  ✓ Updated: {subdir}/{html_file.name}")
                    modified_count += 1
                else:
                    print(f"  - No changes: {subdir}/{html_file.name}")
    
    print(f"\n{'='*50}")
    print(f"Total files modified: {modified_count}")

if __name__ == "__main__":
    main()
