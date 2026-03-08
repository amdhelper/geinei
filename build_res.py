import os
import re

html_path = 'resources.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# All top-level IDs
top_level_ids = [
    'process-guide', 'gear-types', 'forming-methods', 'pm-vs-cnc',
    'surface-treatment', 'design-guide', 'bearings-guide', 'sintering-guide',
    'powder-production', 'quality-control', 'density-porosity', 'faq',
    'glossary', 'materials'
]

# Map each top-level ID to the file it belongs to
file_map = {
    'process-guide': 'resource-process.html',
    'forming-methods': 'resource-process.html',
    'pm-vs-cnc': 'resource-process.html',
    
    'gear-types': 'resource-design.html',
    'design-guide': 'resource-design.html',
    'bearings-guide': 'resource-design.html',
    
    'materials': 'resource-materials.html',
    'surface-treatment': 'resource-materials.html',
    'density-porosity': 'resource-materials.html',
    'sintering-guide': 'resource-materials.html',
    'powder-production': 'resource-materials.html',
    
    'quality-control': 'resource-quality.html',
    
    'faq': 'resource-faq.html',
    'glossary': 'resource-faq.html'
}

# The files and their content blocks
file_content = {k: '' for k in set(file_map.values())}

# Parse top and bottom parts
layout_start_match = re.search(r'(.*?<div class=\"resource-layout\">)', html, re.IGNORECASE | re.DOTALL)
top_part = layout_start_match.group(1) if layout_start_match else ''

aside_match = re.search(r'(<aside class=\"resource-sidebar\">.*?<\/aside>\s*<div class=\"resource-content\">)', html, re.IGNORECASE | re.DOTALL)
aside_part = aside_match.group(1) if aside_match else ''

footer_match = re.search(r'(<\/div>\s*<\/div>\s*<\/section>\s*<!-- Footer -->.*)', html, re.IGNORECASE | re.DOTALL)
footer_part = footer_match.group(1) if footer_match else ''


# Simple DIV balancer
import bs4 # just kidding, let's do simple balancer on the content block
content_start = html.find('<div class=\"resource-content\">') + len('<div class=\"resource-content\">')
content_end = html.find('</div>\n            </div>\n        </section>\n\n        <!-- Footer -->')
content_area = html[content_start:content_end]

lines = content_area.split('\\n')

# Find the start and end of each top-level block
blocks = {}
current_id = None
current_html = []
div_level = 0

for line in lines:
    # check for top level start
    if current_id is None:
        for tid in top_level_ids:
            if f'<div id=\"{tid}\"' in line:
                current_id = tid
                div_level = line.count('<div') - line.count('</div')
                current_html.append(line)
                break
        
        # If we didn't start a block, we ignore or append to some pre-content
        # Actually any pre-content (like <!-- NEW SECTION -->) should just be grabbed beforehand
        if current_id is None and line.strip() != '':
            # Just ignore comments before blocks
            pass
            
    else:
        current_html.append(line)
        div_level += line.count('<div') - line.count('</div')
        if div_level == 0:
            blocks[current_id] = '\\n'.join(current_html)
            
            # Look for leading comments backwards in the original string?
            # actually we can just find where it starts exactly in the content_area
            start_idx = content_area.find('<div id=\"' + current_id + '\"')
            end_idx = start_idx + len(blocks[current_id])
            
            # The comment before it
            prev_block_end = 0
            # Just manually find the comment if it exists
            
            current_id = None
            current_html = []

# Now, a more robust way: use the original content_area string and index finding, combined with div balancing
def extract_block(full_html, block_id):
    start_str = f'<div id=\"{block_id}\"'
    start_idx = full_html.find(start_str)
    if start_idx == -1:
        return ""
        
    # include the comment before it if it exists
    comment_search = full_html.rfind('<!--', 0, start_idx)
    if comment_search != -1 and full_html[comment_search:start_idx].strip().startswith('<!--'):
        actual_start = comment_search
    else:
        actual_start = start_idx

    end_idx = start_idx
    div_count = 0
    in_block = False
    
    # We will iterate through the string
    i = start_idx
    while i < len(full_html):
        if full_html[i:i+4] == '<div':
            div_count += 1
            in_block = True
            i += 4
            continue
        if full_html[i:i+5] == '</div':
            div_count -= 1
            i += 5
            if in_block and div_count == 0:
                end_idx = i + 1 # include the >
                # fast forward to >
                while end_idx < len(full_html) and full_html[end_idx-1] != '>':
                    end_idx += 1
                break
            continue
        i += 1
        
    return full_html[actual_start:end_idx]

for tid in top_level_ids:
    block_html = extract_block(content_area, tid)
    if block_html:
        file_content[file_map[tid]] += '\\n' + block_html + '\\n'
    else:
        print(f"Failed to find {tid}")

# Update sidebar links for every generated page
new_aside = aside_part
for tid, filename in file_map.items():
    new_aside = re.sub(f'href=\"#({tid})\"', f'href=\"{filename}#\\1\"', new_aside)

sub_item_map = {
    'spur-helical': 'resource-design.html',
    'bevel-worm': 'resource-design.html',
    'planetary': 'resource-design.html',
    'press-sinter': 'resource-process.html',
    'mim': 'resource-process.html',
    'hip-forging': 'resource-process.html',
    'iron-steel': 'resource-materials.html',
    'stainless': 'resource-materials.html',
    'magnetic': 'resource-materials.html',
    'bronze-brass': 'resource-materials.html'
}

for div_id, filename in sub_item_map.items():
    new_aside = re.sub(f'href=\"#({div_id})\"', f'href=\"{filename}#\\1\"', new_aside)

# Save the 5 detail pages
for filename, content in file_content.items():
    out_html = top_part + new_aside + content + footer_part
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(out_html)

print("Generated 5 detail pages")

# Now generate the card grid for resources.html
# First, trim the top part to remove the "Technical Resources" header, we'll replace it
nav_end_match = re.search(r'(.*?<\/nav>)', html, re.IGNORECASE | re.DOTALL)
nav_part = nav_end_match.group(1) if nav_end_match else top_part

cards_html = nav_part + '''
    <!-- Hero Section -->
    <section style=\"background: linear-gradient(135deg, #002FA7 0%, #001a6e 100%); padding: 80px 0; text-align: center;\">
        <div class=\"container\">
            <h1 style=\"font-family: 'Playfair Display', serif; font-size: 48px; font-weight: 700; color: white; margin-bottom: 20px;\">
                Technical Resources
            </h1>
            <p style=\"font-size: 20px; color: #a0b0d0; max-width: 700px; margin: 0 auto; line-height: 1.6;\">
                Knowledge Base & FAQ. Explore common questions, material specs, and design guides for Powder Metallurgy.
            </p>
        </div>
    </section>

    <!-- Resources Grid -->
    <section style=\"padding: 80px 0; background: #f8f9fa;\">
        <div class=\"container\">
            <div style=\"display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px;\">

                <!-- Card 1: Process -->
                <a href=\"resource-process.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('images/thumb_res_process.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">Compare & Select</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">Process Selection Guide</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            PM vs CNC Machining vs Casting. Learn about different forming methods including Press & Sinter, MIM, and Forging.
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">Explore →</span>
                    </div>
                </a>

                <!-- Card 2: Design -->
                <a href=\"resource-design.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('images/thumb_res_design.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">Engineering</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">Design & Gear Guides</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            Complete guide to gear types, designing for PM manufacturing, and self-lubricating bearing applications.
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">Explore →</span>
                    </div>
                </a>

                <!-- Card 3: Materials -->
                <a href=\"resource-materials.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('images/thumb_res_material.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">Specs & Treatements</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">Material Specifications</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            Iron, steel, brass, and stainless specs. Details on density, porosity, surface treatments, and powder production.
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">Explore →</span>
                    </div>
                </a>

                <!-- Card 4: Quality -->
                <a href=\"resource-quality.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('images/thumb_res_quality.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">Inspection</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">Quality Control</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            Our systematic approach to ensuring precision, including CMM, optical inspection, and materials testing.
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">Explore →</span>
                    </div>
                </a>

                <!-- Card 5: FAQ & Glossary -->
                <a href=\"resource-faq.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('images/thumb_res_faq.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">Knowledge Base</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">FAQ & Glossary</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            Answers to common questions about PM strength and cost, plus a comprehensive glossary of PM terminology.
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">Explore →</span>
                    </div>
                </a>
                
            </div>
            
            <style>
            .case-card-link:hover {
                transform: translateY(-5px) !important;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1) !important;
            }
            </style>
        </div>
    </section>
'''

with open('resources.html', 'w', encoding='utf-8') as f:
    f.write(cards_html + footer_part)

print("Updated resources.html hub page")
