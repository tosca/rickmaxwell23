from PIL import Image
import os

src = "homeImage-2.jpg"
out_jpeg = "homeImage-2-opt.jpg"
out_webp = "homeImage-2.webp"
max_width = 1920
jpeg_quality = 75
webp_quality = 75

def format_bytes(n):
    return str(n)

# Ensure source exists
if not os.path.exists(src):
    raise SystemExit(f"Source file not found: {src}")

orig_size = os.path.getsize(src)

with Image.open(src) as im:
    orig_w, orig_h = im.size
    print(f"Original path: {os.path.abspath(src)}")
    print(f"Original size (bytes): {format_bytes(orig_size)}")
    print(f"Original dimensions: {orig_w}x{orig_h}")

    # Only resize if wider than max_width
    if orig_w > max_width:
        new_w = max_width
        new_h = int(max_width * orig_h / orig_w)
        im_resized = im.resize((new_w, new_h), Image.LANCZOS)
        print(f"Resized to: {new_w}x{new_h}")
    else:
        im_resized = im.copy()
        print("No resize needed (width <= max)")

    # Convert to RGB if necessary for JPEG
    if im_resized.mode in ("RGBA", "P"):
        im_rgb = im_resized.convert("RGB")
    else:
        im_rgb = im_resized

    # Save optimized JPEG
    im_rgb.save(out_jpeg, "JPEG", quality=jpeg_quality, optimize=True, progressive=True)
    jpeg_size = os.path.getsize(out_jpeg)
    print(f"Saved JPEG path: {os.path.abspath(out_jpeg)}")
    print(f"JPEG size (bytes): {format_bytes(jpeg_size)}")

    # Save WebP
    im_rgb.save(out_webp, "WEBP", quality=webp_quality, method=6)
    webp_size = os.path.getsize(out_webp)
    print(f"Saved WebP path: {os.path.abspath(out_webp)}")
    print(f"WebP size (bytes): {format_bytes(webp_size)}")

    # Summary line
    print("SUMMARY:")
    print(f"{os.path.abspath(src)} {orig_size}")
    print(f"{os.path.abspath(out_jpeg)} {jpeg_size}")
    print(f"{os.path.abspath(out_webp)} {webp_size}")
