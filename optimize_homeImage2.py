from PIL import Image
from pathlib import Path
import os

SOURCE_ROOT = Path("img")
HOME_SOURCE = Path("homeImage-2.jpg")
MAX_WIDTH = 1920
JPEG_QUALITY = 75
WEBP_QUALITY = 75

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def format_bytes(n: int) -> str:
    return f"{n:,} bytes"


def resize_image(im: Image.Image) -> Image.Image:
    orig_w, orig_h = im.size
    if orig_w <= MAX_WIDTH:
        return im.copy()

    new_w = MAX_WIDTH
    new_h = int(MAX_WIDTH * orig_h / orig_w)
    return im.resize((new_w, new_h), Image.LANCZOS)


def save_webp(image: Image.Image, out_path: Path) -> int:
    image.save(out_path, "WEBP", quality=WEBP_QUALITY, method=6)
    return out_path.stat().st_size


def save_jpeg(image: Image.Image, out_path: Path) -> int:
    image.save(out_path, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    return out_path.stat().st_size


def process_path(path: Path) -> None:
    print(f"Processing: {path}")
    orig_size = path.stat().st_size

    with Image.open(path) as im:
        im_resized = resize_image(im)
        if im_resized.mode in ("RGBA", "P"):
            im_rgb = im_resized.convert("RGB")
        else:
            im_rgb = im_resized

        webp_path = path.with_suffix(".webp")
        webp_size = save_webp(im_rgb, webp_path)
        print(f"  -> WebP: {webp_path} ({format_bytes(webp_size)})")

        if path.suffix.lower() in {".jpg", ".jpeg"}:
            optimized_jpeg_path = path.with_name(path.stem + "-opt.jpg")
            jpeg_size = save_jpeg(im_rgb, optimized_jpeg_path)
            print(f"  -> Optimized JPEG: {optimized_jpeg_path} ({format_bytes(jpeg_size)})")

    print(f"  Original: {path} ({format_bytes(orig_size)})\n")


if __name__ == "__main__":
    if HOME_SOURCE.exists():
        process_path(HOME_SOURCE)

    for path in SOURCE_ROOT.rglob("*"):
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            process_path(path)

    print("Done. Generated WebP variants for supported images.")
