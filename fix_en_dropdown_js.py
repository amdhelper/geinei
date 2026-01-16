import os
import re

# English pages in root directory that need the JavaScript fix
PAGES = ['about.html', 'products.html', 'contact.html', 'solutions.html', 
         'capabilities.html', 'applications.html', 'resources.html', 'emerging-tech.html']

# JavaScript to add before </body>
JS_CODE = '''
    <script>
        function toggleLangDropdown() {
            var dropdown = document.getElementById("langDropdown");
            if (dropdown) {
                dropdown.style.display = (dropdown.style.display === "none" || dropdown.style.display === "") ? "block" : "none";
            }
        }
        document.addEventListener('click', function(e) {
            var dropdown = document.getElementById("langDropdown");
            if (dropdown && !e.target.closest('#langDropdown') && !e.target.matches('[onclick="toggleLangDropdown()"]')) {
                dropdown.style.display = "none";
            }
        });
    </script>
'''

def update_file(filepath):
    page_name = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if toggleLangDropdown already exists
    if 'function toggleLangDropdown' in content:
        print(f"  Already has function: {page_name}")
        return False
    
    # Check if the page uses toggleLangDropdown
    if 'toggleLangDropdown()' not in content:
        print(f"  No toggle call found: {page_name}")
        return False
    
    # Add JS before </body>
    if '</body>' in content:
        new_content = content.replace('</body>', JS_CODE + '</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Updated: {page_name}")
        return True
    else:
        print(f"  No </body> found: {page_name}")
        return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    updated_count = 0
    
    print("Adding toggleLangDropdown JavaScript to English pages...")
    
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
