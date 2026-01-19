#!/usr/bin/env python3
"""
Script to add hreflang tags to all multi-language HTML pages.
Fixes Google Search Console indexing issues by properly identifying language versions.
"""

import os
import re
from pathlib import Path

# Base URL
BASE_URL = "https://yehsheng.com"

# Language directories and their hreflang codes
LANG_DIRS = {
    "de": "de",
    "jp": "ja",
    "zh": "zh-Hant",
    "zh-cn": "zh-Hans"
}

# Pages to process (excluding 404.html)
PAGES = [
    "index.html",
    "about.html", 
    "products.html",
    "solutions.html",
    "capabilities.html",
    "applications.html",
    "emerging-tech.html",
    "contact.html",
    "resources.html"
]

def generate_hreflang_tags(page_name):
    """Generate hreflang tags for a given page."""
    tags = []
    tags.append('    <!-- hreflang tags for multilingual SEO -->')
    tags.append(f'    <link rel="alternate" hreflang="en" href="{BASE_URL}/{page_name}" />')
    tags.append(f'    <link rel="alternate" hreflang="zh-Hant" href="{BASE_URL}/zh/{page_name}" />')
    tags.append(f'    <link rel="alternate" hreflang="zh-Hans" href="{BASE_URL}/zh-cn/{page_name}" />')
    tags.append(f'    <link rel="alternate" hreflang="de" href="{BASE_URL}/de/{page_name}" />')
    tags.append(f'    <link rel="alternate" hreflang="ja" href="{BASE_URL}/jp/{page_name}" />')
    tags.append(f'    <link rel="alternate" hreflang="x-default" href="{BASE_URL}/{page_name}" />')
    return '\n'.join(tags)

def add_hreflang_to_file(file_path, page_name):
    """Add hreflang tags to a single HTML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if hreflang already exists
    if 'hreflang' in content:
        print(f"  ⏭️  Skipping {file_path} - hreflang already exists")
        return False
    
    # Find the canonical tag and insert hreflang after it
    canonical_pattern = r'(<link[^>]*rel="canonical"[^>]*/?>)'
    match = re.search(canonical_pattern, content)
    
    if match:
        canonical_tag = match.group(1)
        hreflang_tags = generate_hreflang_tags(page_name)
        new_content = content.replace(
            canonical_tag,
            canonical_tag + '\n' + hreflang_tags
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ Added hreflang to {file_path}")
        return True
    else:
        print(f"  ⚠️  No canonical tag found in {file_path}")
        return False

def main():
    """Main function to process all language directories."""
    base_dir = Path(__file__).parent
    
    total_modified = 0
    total_skipped = 0
    
    for lang_dir in LANG_DIRS.keys():
        print(f"\n📁 Processing {lang_dir}/ directory...")
        dir_path = base_dir / lang_dir
        
        if not dir_path.exists():
            print(f"  ❌ Directory not found: {dir_path}")
            continue
        
        for page in PAGES:
            file_path = dir_path / page
            if file_path.exists():
                if add_hreflang_to_file(file_path, page):
                    total_modified += 1
                else:
                    total_skipped += 1
            else:
                print(f"  ⚠️  File not found: {file_path}")
    
    print(f"\n{'='*50}")
    print(f"✅ Total files modified: {total_modified}")
    print(f"⏭️  Total files skipped: {total_skipped}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
