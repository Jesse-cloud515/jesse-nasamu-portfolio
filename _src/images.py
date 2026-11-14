"""Convert original images into optimised WebP sizes. Usage: python3 images.py <orig_img_dir> <site_root>"""
import sys, os
from PIL import Image
SRC, ROOT = sys.argv[1], sys.argv[2]
P = os.path.join(SRC, "portfolio")
MAP = {
 # work/<name>: source file
 "work/cyber-awareness-1": "sec1.jpg", "work/cyber-awareness-2": "sec.jpg", "work/cyber-awareness-3": "sec2.jpg",
 "work/cyber-awareness-4": "app.jpg", "work/cyber-awareness-5": "Cyb1.jpg",
 "work/michalo-1": "michalo.png", "work/michalo-2": "Frame 3.png",
 "work/preview-1": "PreView@2x.jpg", "work/preview-2": "PreView.jpg", "work/preview-3": "Frame 31.jpg", "work/preview-4": "Frame 32.jpg",
 "work/sb4kids-1": "sb4kids1.jpg", "work/sb4kids-2": "sb4kids2.jpg", "work/sb4kids-3": "sb4kids3.jpg",
 "work/sb4kids-4": "NITDA2.jpg", "work/sb4kids-5": "NITDA1.jpg",
 "work/sheriff-1": "Frame 44.jpg", "work/sheriff-2": "Frame 43.jpg", "work/sheriff-3": "Frame 40.jpg", "work/sheriff-4": "Frame 42.jpg", "work/sheriff-5": "skaterboy.jpg",
 "work/bike-sales-1": "Analysis 4.png", "work/bike-sales-2": "Analysis 2.png",
 "work/regional-sales-1": "Analysis 3.png",
 "work/customer-segmentation-1": "Analysis 1.png",
 "work/aficat-1": "AFICAT (FUJIKEN).jpg", "work/aficat-2": "Backdrop.jpg", "work/aficat-3": "Backdrop4.jpg", "work/aficat-4": "Backdrop2.jpg",
 "work/fraud-1": "Fraud Detection.png",
 "work/cyber-overview": "/mnt/user-data/uploads/Data Analysis/Project/Cyber Security Attacks/Images/1_dashboard_executive_overview.png",
 "work/cyber-model": "/mnt/user-data/uploads/Data Analysis/Project/Cyber Security Attacks/Images/3_data_model.png",
 "gallery/eid": "minimalismo.jpg", "gallery/adopt-a-dog": "rucksack.png", "gallery/chick-co": "sanddunes.jpg",
 "gallery/danfo": "Frame 20.jpg", "gallery/africa-1": "Frame 21.jpg", "gallery/africa-2": "Frame 22.jpg",
 "gallery/africa-3": "Frame 23.jpg", "gallery/africa-4": "Frame 24.jpg",

}
sizes = {}
for out, src in MAP.items():
    im = Image.open(src if src.startswith("/") else os.path.join(P, src)).convert("RGB")
    for w in (800, 1600):
        c = im.copy()
        if c.width > w: c = c.resize((w, round(c.height * w / c.width)), Image.LANCZOS)
        c.save(os.path.join(ROOT, "assets/img", f"{out}-{w}.webp"), "WEBP", quality=(90 if out.startswith("work/cyber") or out.startswith("work/fraud") else 80), method=6)
    sizes[out] = (im.width, im.height)
im = Image.open(os.path.join(SRC, "profile/about-photo.jpg")).convert("RGB")
im.save(os.path.join(ROOT, "assets/img/jesse-nasamu.webp"), "WEBP", quality=86, method=6)
im.save(os.path.join(ROOT, "assets/img/jesse-nasamu.jpg"), "JPEG", quality=88)
# Open Graph image 1200x630: portrait on ink
og = Image.new("RGB", (1200, 630), (14, 27, 34)); p = im.copy(); p.thumbnail((504, 630)); og.paste(p, (1200 - p.width, 0))
og.save(os.path.join(ROOT, "assets/img/og-image.jpg"), quality=85)
for f in ["favicon-32x32.png", "favicon-16x16.png", "apple-touch-icon.png", "android-chrome-192x192.png", "android-chrome-512x512.png"]:
    Image.open(os.path.join(SRC, f)).save(os.path.join(ROOT, "assets/img", f))
import json; json.dump(sizes, open(os.path.join(ROOT, "_src/image-sizes.json"), "w"), indent=1)
print(len(MAP), "images done")
