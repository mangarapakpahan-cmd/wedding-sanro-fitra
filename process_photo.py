from PIL import Image
import os

source_path = r"C:\Users\manga\.gemini\antigravity\brain\8b05d08c-6e35-49c3-952a-8e639479e5ca\.user_uploaded\media_1792461116182_d311046b.jpg"
target_dir = r"C:\Users\manga\.gemini\antigravity\scratch\wedding-sanro-fitra\assets\images"
os.makedirs(target_dir, exist_ok=True)

img = Image.open(source_path)
width, height = img.size

# 1. Full image
img.save(os.path.join(target_dir, "couple-full.jpg"), quality=95)
img.save(os.path.join(target_dir, "hero-cover.jpg"), quality=95)

# 2. Portrait Crop (centered on the couple with Danau Toba mountains above)
# Couple is around center x: 450 to 600, y: 340 to 560
# Let's crop a 3:4 portrait: width around 420, height 560
left = int(width * 0.35)   # ~358
right = int(width * 0.76)  # ~778
top = int(height * 0.15)   # ~85
bottom = height            # 571

portrait_crop = img.crop((left, top, right, bottom))
portrait_crop.save(os.path.join(target_dir, "couple-portrait.jpg"), quality=95)

# 3. Square Crop for Mempelai section
# Centered closely on Sanro & Fitra
crop_size = min(int(height * 0.75), 400)
center_x = int(width * 0.525)
center_y = int(height * 0.62)
sq_left = max(0, center_x - crop_size // 2)
sq_right = min(width, center_x + crop_size // 2)
sq_top = max(0, center_y - crop_size // 2)
sq_bottom = min(height, center_y + crop_size // 2)

square_crop = img.crop((sq_left, sq_top, sq_right, sq_bottom))
square_crop.save(os.path.join(target_dir, "couple-square.jpg"), quality=95)

print("Saved couple-full.jpg, couple-portrait.jpg, couple-square.jpg successfully!")
