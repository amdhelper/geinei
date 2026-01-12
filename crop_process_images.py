from PIL import Image
import os

def crop_images():
    source_path = '/home/ubuntu/pure_html/images/production-process-real.jpg'
    output_dir = '/home/ubuntu/pure_html/images'
    
    if not os.path.exists(source_path):
        print(f"Error: {source_path} not found")
        return

    img = Image.open(source_path)
    width, height = img.size
    
    # The image has 5 steps distributed horizontally
    # Total width 1000. Each step is approx 200px.
    # We will crop them into 5 equal parts.
    
    step_width = width // 5
    
    steps = ['powder', 'press', 'sintered', 'sizing', 'secondary']
    
    for i, step_name in enumerate(steps):
        left = i * step_width
        right = (i + 1) * step_width
        # Crop the full height
        box = (left, 0, right, height)
        
        # Optional: Crop a bit of margin to avoid bleeding into next card if they are tight
        # But looking at the image, they seem to have white space. 
        # Let's try to crop the center part of each 200px slot to be safe?
        # No, let's take the full 200px first.
        
        cropped = img.crop(box)
        
        output_filename = f"process-real-{step_name}.jpg"
        output_path = os.path.join(output_dir, output_filename)
        
        cropped.save(output_path)
        print(f"Saved {output_path}")

if __name__ == "__main__":
    crop_images()
