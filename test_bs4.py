import os
from bs4 import BeautifulSoup

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    res_content = soup.find('div', class_='resource-content')
    if not res_content: return
    
    for div in res_content.find_all('div', recursive=False):
        if not div.has_attr('id'): continue
        
        h3 = div.find('h3', recursive=False)
        if not h3: continue
        
        # Change div class
        existing_classes = div.get('class', [])
        if 'accordion-card' not in existing_classes:
            div['class'] = existing_classes + ['accordion-card']
        
        # Remove margin-bottom
        if 'style' in div.attrs:
            div['style'] = div['style'].replace('margin-bottom: 80px;', '').replace('margin-bottom:80px', '')
            if not div['style'].strip() or div['style'].strip() == ';':
                del div['style']
        
        # Create header
        header = soup.new_tag('div', attrs={'class': 'accordion-header', 'onclick': 'toggleAccordion(this)'})
        h3.extract()
        
        # Style h3 for header
        h3['style'] = h3.get('style', '') + '; margin: 0; border: none; padding: 0; font-size: 24px;'
        header.append(h3)
        
        icon = soup.new_tag('span', attrs={'class': 'accordion-icon'})
        icon.string = '🔽'
        header.append(icon)
        
        # Create body wrapper
        body_wrapper = soup.new_tag('div', attrs={'class': 'accordion-body-wrapper'})
        body_inner = soup.new_tag('div', attrs={'class': 'accordion-body-inner'})
        
        # Extract children
        for child in list(div.contents):
            child.extract()
            body_inner.append(child)
            
        body_wrapper.append(body_inner)
        div.append(header)
        div.append(body_wrapper)
    
    # Inject CSS
    head = soup.find('head')
    if head:
        css = soup.new_tag('style')
        css.string = '''
        .accordion-card {
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 25px;
            overflow: hidden;
            border: 1px solid #eee;
            transition: all 0.3s ease;
        }
        .accordion-card:hover {
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            transform: translateY(-2px);
        }
        .accordion-header {
            padding: 20px 30px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #fdfbf7;
            border-bottom: 1px solid transparent;
            transition: all 0.3s ease;
        }
        .accordion-card.active .accordion-header {
            border-bottom: 1px solid #eee;
            background: #fff;
        }
        .accordion-icon {
            font-size: 20px;
            color: #C5A059;
            transition: transform 0.3s ease;
        }
        .accordion-card.active .accordion-icon {
            transform: rotate(180deg);
        }
        .accordion-body-wrapper {
            display: grid;
            grid-template-rows: 0fr;
            transition: grid-template-rows 0.3s ease-out;
        }
        .accordion-card.active .accordion-body-wrapper {
            grid-template-rows: 1fr;
        }
        .accordion-body-inner {
            overflow: hidden;
            padding: 0 30px;
            opacity: 0;
            transition: opacity 0.3s ease-out, padding 0.3s ease;
        }
        .accordion-card.active .accordion-body-inner {
            padding: 0 30px 30px 30px;
            opacity: 1;
        }
        /* Mobile adjustment */
        @media (max-width: 768px) {
            .accordion-header { padding: 15px 20px; }
            .accordion-body-inner { padding: 0 20px; }
            .accordion-card.active .accordion-body-inner { padding: 0 20px 20px 20px; }
            .accordion-header h3 { font-size: 20px !important; }
        }
        '''
        head.append(css)
    
    # Inject JS
    body = soup.find('body')
    if body:
        js = soup.new_tag('script')
        js.string = '''
        function toggleAccordion(header) {
            const card = header.closest('.accordion-card');
            
            // Optional: Close others
            // document.querySelectorAll('.accordion-card').forEach(c => {
            //     if (c !== card) c.classList.remove('active');
            // });
            
            card.classList.toggle('active');
        }
        '''
        body.append(js)
        
    with open('test_bs4.html', 'w', encoding='utf-8') as f:
        # Avoid weird escaping issues in beautifulsoup formatting
        f.write(str(soup))
    print(f"Tested on {filepath}")

process_file('resource-process.html')
