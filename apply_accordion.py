import os
from bs4 import BeautifulSoup

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        res_content = soup.find('div', class_='resource-content')
        if not res_content: return
        
        modified = False
        
        for div in res_content.find_all('div', recursive=False):
            if not div.has_attr('id'): continue
            
            h3 = div.find('h3', recursive=False)
            if not h3: continue
            
            # Change div class
            existing_classes = div.get('class', [])
            if 'accordion-card' not in existing_classes:
                div['class'] = existing_classes + ['accordion-card']
                modified = True
            else:
                continue # Already processed
            
            # Remove margin-bottom
            if 'style' in div.attrs:
                div['style'] = div['style'].replace('margin-bottom: 80px;', '').replace('margin-bottom:80px', '')
                if not div['style'].strip() or div['style'].strip() == ';':
                    del div['style']
            
            # Create header
            header = soup.new_tag('div', attrs={'class': 'accordion-header', 'onclick': 'toggleAccordion(this)'})
            h3.extract()
            
            # Reset margins on h3
            h3['style'] = h3.get('style', '') + '; margin: 0 !important; border: none; padding: 0; font-size: 24px;'
            header.append(h3)
            
            icon = soup.new_tag('span', attrs={'class': 'accordion-icon'})
            icon.string = '🔽'
            header.append(icon)
            
            # Create body wrapper
            body_wrapper = soup.new_tag('div', attrs={'class': 'accordion-body-wrapper'})
            body_inner = soup.new_tag('div', attrs={'class': 'accordion-body-inner'})
            
            # Extract children
            for child in list(div.contents):
                if child.name == 'style' and child.string and 'accordion' in child.string: continue
                if child.name == 'script' and child.string and 'toggleAccordion' in child.string: continue
                child.extract()
                body_inner.append(child)
                
            body_wrapper.append(body_inner)
            div.append(header)
            div.append(body_wrapper)
        
        if not modified:
             print(f"Skipped {filepath} (already processed or no sections found)")
             return
             
        # Inject CSS
        head = soup.find('head')
        if head and not head.find(string=lambda t: t and '.accordion-card' in t):
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
                padding: 15px 30px;
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
                padding: 30px 30px 30px 30px;
                opacity: 1;
            }
            /* Mobile adjustment */
            @media (max-width: 768px) {
                .accordion-header { padding: 15px 20px; }
                .accordion-body-inner { padding: 0 20px; }
                .accordion-card.active .accordion-body-inner { padding: 20px; }
                .accordion-header h3 { font-size: 20px !important; }
            }
            '''
            head.append(css)
        
        # Inject JS
        body = soup.find('body')
        if body and not body.find(string=lambda t: t and 'function toggleAccordion' in t):
            js = soup.new_tag('script')
            js.string = '''
            function toggleAccordion(header) {
                const card = header.closest('.accordion-card');
                card.classList.toggle('active');
            }
            
            function openAccordionFromHash() {
                if (window.location.hash) {
                    const target = document.querySelector(window.location.hash);
                    if (target && target.classList.contains('accordion-card')) {
                        target.classList.add('active');
                        setTimeout(() => {
                            const offsetTop = target.getBoundingClientRect().top + window.scrollY - 120;
                            window.scrollTo({ top: offsetTop, behavior: 'smooth' });
                        }, 300); // Wait for transition
                    }
                }
            }
            
            window.addEventListener('hashchange', openAccordionFromHash);
            document.addEventListener('DOMContentLoaded', function() {
                openAccordionFromHash();
                
                // Intercept sidebar clicks
                document.querySelectorAll('.sidebar-nav a').forEach(anchor => {
                    anchor.addEventListener('click', function (e) {
                        const href = this.getAttribute('href');
                        if (href && href.includes('#')) {
                            const targetId = href.split('#')[1];
                            const targetElement = document.getElementById(targetId);
                            if (targetElement && targetElement.classList.contains('accordion-card')) {
                                targetElement.classList.add('active');
                            }
                        }
                    });
                });
            });
            '''
            body.append(js)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Applied accordion to {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

langs = ['', 'zh/', 'zh-cn/', 'de/', 'jp/']
pages = ['resource-process.html', 'resource-design.html', 'resource-materials.html', 'resource-quality.html', 'resource-faq.html']

for lang in langs:
    for page in pages:
        filepath = os.path.join(lang, page)
        if os.path.exists(filepath):
            process_file(filepath)
