import os
import re
from pathlib import Path

def check_images(directory):
    print(f"Checking images in {directory}...")
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    for html_file in html_files:
        file_path = os.path.join(directory, html_file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all img src
        images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
        
        print(f"\nChecking {html_file}: {len(images)} images found")
        for img_src in images:
            # Handle absolute links (ignore)
            if img_src.startswith('http') or img_src.startswith('//'):
                continue
                
            # Construct absolute path
            img_path = os.path.join(directory, img_src.replace('/', os.sep))
            
            if not os.path.exists(img_path):
                print(f"  [MISSING] {img_src}")
            else:
                print(f"  [OK] {img_src}")

check_images(r"C:\Users\Caroline Kelly\Downloads\Website Design")
