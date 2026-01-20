#!/usr/bin/env python3
"""
Add Microsoft Clarity tracking script to all HTML pages
"""
import os
import re

BASE_DIR = r"c:\Users\USER\geinei_clean"

CLARITY_SCRIPT = '''    <!-- Microsoft Clarity -->
    <script type="text/javascript">
        (function(c,l,a,r,i,t,y){
            c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
            t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
            y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        })(window, document, "clarity", "script", "q46c2dab8f");
    </script>'''

def add_clarity_to_file(filepath):
    """Add Clarity script after Google Analytics if not already present"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if Clarity already exists
        if 'clarity.ms' in content or 'clarity' in content.lower() and 'microsoft' in content.lower():
            return False
        
        # Find position after Google Analytics script (before </head> or after gtag config)
        # Pattern: after gtag('config', 'G-XS5ZTZGF2Y');
        pattern = r"(gtag\('config', 'G-XS5ZTZGF2Y'\);[\s\r\n]*</script>)"
        
        if re.search(pattern, content):
            new_content = re.sub(pattern, r'\1\n' + CLARITY_SCRIPT, content)
        else:
            # Alternative: insert before </head>
            new_content = content.replace('</head>', CLARITY_SCRIPT + '\n</head>')
        
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
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    print("=== Adding Microsoft Clarity to all pages ===")
    html_files = find_all_html_files()
    updated_count = 0
    
    for filepath in html_files:
        if add_clarity_to_file(filepath):
            print(f"✓ Updated: {filepath}")
            updated_count += 1
    
    print(f"\nTotal files updated: {updated_count}")

if __name__ == "__main__":
    main()
