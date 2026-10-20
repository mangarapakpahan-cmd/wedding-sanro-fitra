from PIL import Image
import os

source_path = r"C:\Users\manga\.gemini\antigravity\brain\8b05d08c-6e35-49c3-952a-8e639479e5ca\.user_uploaded\media_1792461116182_d311046b.jpg"
target_dir = r"C:\Users\manga\.gemini\antigravity\scratch\wedding-sanro-fitra\assets\images"

img = Image.open(source_path)
width, height = img.size
# width: 1024, height: 571

# Sanro is seated left center: roughly x=460..555, y=340..560
# Sanro bust crop (face & torso):
sanro_crop = img.crop((440, 310, 560, 480))
sanro_crop.save(os.path.join(target_dir, "groom-sanro.jpg"), quality=95)

# Fitra is leaning right center: roughly x=505..600, y=320..500
# Fitra bust crop (face & dress):
fitra_crop = img.crop((500, 310, 610, 480))
fitra_crop.save(os.path.join(target_dir, "bride-fitra.jpg"), quality=95)

# Grand Couple Portrait (Sanro & Fitra together with background):
couple_bust = img.crop((430, 290, 620, 540))
couple_bust.save(os.path.join(target_dir, "couple-bust.jpg"), quality=95)

print("Created groom-sanro.jpg, bride-fitra.jpg, and couple-bust.jpg successfully!")
