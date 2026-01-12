import os
import shutil
import re

# Configuration
ROOT_DIR = '/home/ubuntu/pure_html'
LANGUAGES = ['zh', 'de', 'jp']
FILES_TO_PROCESS = ['index.html', 'products.html', 'solutions.html', 'applications.html', 'capabilities.html', 'emerging-tech.html', 'about.html', 'contact.html']

# Translation Dictionary (Updated for Premium Style & Mobile Menu)
TRANSLATIONS = {
    'zh': {
        'About Us': '關於我們',
        'Contact': '聯絡我們',
        'Contact Us': '聯絡我們',
        'Products': '產品中心',
        'Solutions': '解決方案',
        'Capabilities': '製程能力',
        'Industries': '應用領域',
        'Innovation': '創新技術',
        'Precision in': '極致精密',
        'Every Particle.': '始於微粒。',
        'ISO 9001:2015 Certified': '通過 ISO 9001:2015 認證',
        'Engineering high-performance sintered components with micron-level precision for the automotive and industrial future.': '專注於開發高性能粉末冶金元件，以微米級的精密工藝，賦能汽車與工業的未來。',
        'Explore Products': '探索產品',
        'Contact Engineering': '聯繫工程團隊',
        'Years Experience': '年製造經驗',
        'Precision Tolerance': '精密公差',
        '9001 Certified': '9001 認證',
        'Export Reach': '出口全球',
        'Our Expertise': '專業領域',
        'Driving Future Mobility': '驅動未來移動科技',
        'Automotive Excellence': '汽車工業卓越',
        'Industrial Power': '工業動力核心',
        'Medical Precision': '醫療精密組件',
        'High-precision rotors and structural parts for next-generation automotive applications.': '用於下一代汽車應用的高精度轉子與結構件。',
        'Robust gears and transmission components engineered for heavy-duty machinery.': '專為重型機械設計的強固齒輪與傳動元件。',
        'Biocompatible stainless steel parts for surgical and diagnostic devices.': '用於手術與診斷設備的生物相容性不鏽鋼零件。',
        'View Automotive Parts →': '查看汽車零件 →',
        'View Industrial Parts →': '查看工業零件 →',
        'View Medical Parts →': '查看醫療零件 →',
        'Company': '公司資訊',
        'All Products': '所有產品',
        'Premier manufacturer of high-precision powder metallurgy components since 1980.': '自 1980 年以來的高精密粉末冶金元件領導製造商。',
        'No. 11, Ln. 721, Zhong Zheng Rd.': '新北市新莊區中正路721巷11號',
        'Xin Zhuang Dist., New Taipei City': '24265 台灣',
        'All rights reserved.': '版權所有。',
        'English ▼': '中文 ▼'
    },
    'de': {
        'About Us': 'Über uns',
        'Contact': 'Kontakt',
        'Contact Us': 'Kontakt',
        'Products': 'Produkte',
        'Solutions': 'Lösungen',
        'Capabilities': 'Fähigkeiten',
        'Industries': 'Branchen',
        'Innovation': 'Innovation',
        'Precision in': 'Präzision in',
        'Every Particle.': 'Jedem Partikel.',
        'ISO 9001:2015 Certified': 'ISO 9001:2015 Zertifiziert',
        'Engineering high-performance sintered components with micron-level precision for the automotive and industrial future.': 'Entwicklung von Hochleistungs-Sinterkomponenten mit mikrometergenauer Präzision für die Zukunft der Automobil- und Industriebranche.',
        'Explore Products': 'Produkte entdecken',
        'Contact Engineering': 'Ingenieurteam kontaktieren',
        'Years Experience': 'Jahre Erfahrung',
        'Precision Tolerance': 'Präzisionstoleranz',
        '9001 Certified': '9001 Zertifiziert',
        'Export Reach': 'Globaler Export',
        'Our Expertise': 'Unsere Expertise',
        'Driving Future Mobility': 'Antrieb der Zukunft',
        'Automotive Excellence': 'Automobil-Exzellenz',
        'Industrial Power': 'Industrielle Kraft',
        'Medical Precision': 'Medizinische Präzision',
        'High-precision rotors and structural parts for next-generation automotive applications.': 'Hochpräzise Rotoren und Strukturteile für Automobilanwendungen der nächsten Generation.',
        'Robust gears and transmission components engineered for heavy-duty machinery.': 'Robuste Zahnräder und Getriebekomponenten für Schwermaschinen.',
        'Biocompatible stainless steel parts for surgical and diagnostic devices.': 'Biokompatible Edelstahlteile für chirurgische und diagnostische Geräte.',
        'View Automotive Parts →': 'Automobilteile ansehen →',
        'View Industrial Parts →': 'Industrieteile ansehen →',
        'View Medical Parts →': 'Medizinteile ansehen →',
        'Company': 'Unternehmen',
        'All Products': 'Alle Produkte',
        'Premier manufacturer of high-precision powder metallurgy components since 1980.': 'Führender Hersteller von hochpräzisen pulvermetallurgischen Komponenten seit 1980.',
        'No. 11, Ln. 721, Zhong Zheng Rd.': 'No. 11, Ln. 721, Zhong Zheng Rd.',
        'Xin Zhuang Dist., New Taipei City': 'Xin Zhuang Dist., New Taipei City, Taiwan',
        'All rights reserved.': 'Alle Rechte vorbehalten.',
        'English ▼': 'Deutsch ▼'
    },
    'jp': {
        'About Us': '会社概要',
        'Contact': 'お問い合わせ',
        'Contact Us': 'お問い合わせ',
        'Products': '製品情報',
        'Solutions': 'ソリューション',
        'Capabilities': '技術力',
        'Industries': '適用分野',
        'Innovation': '革新技術',
        'Precision in': '極限の精度を',
        'Every Particle.': 'すべての粒子に。',
        'ISO 9001:2015 Certified': 'ISO 9001:2015 認証取得',
        'Engineering high-performance sintered components with micron-level precision for the automotive and industrial future.': '自動車および産業の未来のために、ミクロンレベルの精度を持つ高性能焼結部品を設計・製造します。',
        'Explore Products': '製品を見る',
        'Contact Engineering': '技術相談はこちら',
        'Years Experience': '年の経験',
        'Precision Tolerance': '精密公差',
        '9001 Certified': '9001 認証',
        'Export Reach': 'グローバル展開',
        'Our Expertise': '専門分野',
        'Driving Future Mobility': '未来のモビリティを駆動する',
        'Automotive Excellence': '自動車産業の卓越性',
        'Industrial Power': '産業機械の動力',
        'Medical Precision': '医療機器の精密さ',
        'High-precision rotors and structural parts for next-generation automotive applications.': '次世代自動車アプリケーション向けの高精度ローターおよび構造部品。',
        'Robust gears and transmission components engineered for heavy-duty machinery.': '重機向けに設計された堅牢なギアおよびトランスミッション部品。',
        'Biocompatible stainless steel parts for surgical and diagnostic devices.': '手術および診断装置向けの生体適合性ステンレス鋼部品。',
        'View Automotive Parts →': '自動車部品を見る →',
        'View Industrial Parts →': '産業部品を見る →',
        'View Medical Parts →': '医療部品を見る →',
        'Company': '会社情報',
        'All Products': '全製品',
        'Premier manufacturer of high-precision powder metallurgy components since 1980.': '1980年創業、高精度粉末冶金部品のリーディングメーカー。',
        'No. 11, Ln. 721, Zhong Zheng Rd.': '台湾新北市新荘区中正路721巷11号',
        'Xin Zhuang Dist., New Taipei City': '24265 台湾',
        'All rights reserved.': 'All rights reserved.',
        'English ▼': '日本語 ▼'
    }
}

def translate_content(content, lang_code):
    """Replace English text with translated text based on dictionary."""
    translations = TRANSLATIONS.get(lang_code, {})
    
    # Sort keys by length (descending) to prevent partial replacements
    sorted_keys = sorted(translations.keys(), key=len, reverse=True)
    
    for key in sorted_keys:
        # Use simple string replacement for reliability with inline styles
        pattern = re.compile(re.escape(key), re.IGNORECASE)
        content = content.replace(key, translations[key])
        
    return content

def fix_paths(content):
    """Update relative paths for assets when moving to subdirectories."""
    content = content.replace('href="about.html"', 'href="../about.html"')
    content = content.replace('href="contact.html"', 'href="../contact.html"')
    content = content.replace('href="products.html"', 'href="../products.html"')
    content = content.replace('href="solutions.html"', 'href="../solutions.html"')
    content = content.replace('href="capabilities.html"', 'href="../capabilities.html"')
    content = content.replace('href="applications.html"', 'href="../applications.html"')
    content = content.replace('href="emerging-tech.html"', 'href="../emerging-tech.html"')
    content = content.replace('href="index.html"', 'href="../index.html"')
    
    # Fix images and css
    content = content.replace('src="images/', 'src="../images/')
    content = content.replace('href="assets/', 'href="../assets/')
    
    # Fix language switcher links
    content = content.replace('href="zh/index.html"', 'href="../zh/index.html"')
    content = content.replace('href="de/index.html"', 'href="../de/index.html"')
    content = content.replace('href="jp/index.html"', 'href="../jp/index.html"')
    
    return content

def main():
    for lang in LANGUAGES:
        lang_dir = os.path.join(ROOT_DIR, lang)
        
        # Create language directory if not exists
        if not os.path.exists(lang_dir):
            os.makedirs(lang_dir)
            
        print(f"Generating {lang} pages in {lang_dir}...")
        
        for filename in FILES_TO_PROCESS:
            src_path = os.path.join(ROOT_DIR, filename)
            dest_path = os.path.join(lang_dir, filename)
            
            if os.path.exists(src_path):
                with open(src_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Translate
                translated_content = translate_content(content, lang)
                
                # 2. Fix Paths
                final_content = fix_paths(translated_content)
                
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(final_content)
                
                print(f"Generated {dest_path}")

if __name__ == "__main__":
    main()
