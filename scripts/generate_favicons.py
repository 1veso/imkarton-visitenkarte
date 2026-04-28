"""Generate favicon raster assets from the box icon geometry.

Renders at high resolution with Pillow, then downsamples for crisp small sizes.
"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

BG = (247, 245, 240, 255)
STROKE = (43, 110, 143, 255)

# Geometry in a 100x100 viewBox (matches favicon.svg).
PATHS = [
    [(14, 48), (56, 48), (56, 88), (14, 88), (14, 48)],
    [(35, 48), (35, 88)],
    [(56, 48), (84, 36), (84, 76), (56, 88), (56, 48)],
    [(70, 42), (70, 82)],
    [(14, 48), (28, 22), (46, 32)],
    [(46, 32), (58, 14), (74, 20)],
    [(74, 20), (84, 36)],
    [(46, 32), (56, 48)],
    [(28, 22), (56, 48)],
    [(74, 20), (56, 48)],
]


def render(size: int, *, transparent_bg: bool = False) -> Image.Image:
    # Render at 8x for super-sampling, then downsample.
    SS = 8
    px = size * SS
    if transparent_bg:
        img = Image.new("RGBA", (px, px), (0, 0, 0, 0))
    else:
        img = Image.new("RGBA", (px, px), BG)
    draw = ImageDraw.Draw(img)

    scale = px / 100.0
    # Stroke proportional to viewBox (8 units wide), but never thinner than 2 final px.
    stroke_w = max(int(round(8 * scale)), SS * 2)

    for path in PATHS:
        pts = [(x * scale, y * scale) for (x, y) in path]
        draw.line(pts, fill=STROKE, width=stroke_w, joint="curve")
        # Cap each endpoint with a circle to mimic stroke-linecap=round.
        r = stroke_w // 2
        for x, y in pts:
            draw.ellipse((x - r, y - r, x + r, y + r), fill=STROKE)

    return img.resize((size, size), Image.LANCZOS)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)

    f16 = render(16)
    f32 = render(32)
    f180 = render(180)

    f16.save(ASSETS / "favicon-16x16.png", optimize=True)
    f32.save(ASSETS / "favicon-32x32.png", optimize=True)
    f180.save(ASSETS / "apple-touch-icon.png", optimize=True)

    # Multi-resolution ICO with 16 and 32.
    f32.save(
        ROOT / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32)],
    )

    print("favicons generated:")
    print(f"  {ASSETS / 'favicon-16x16.png'}")
    print(f"  {ASSETS / 'favicon-32x32.png'}")
    print(f"  {ASSETS / 'apple-touch-icon.png'}")
    print(f"  {ROOT / 'favicon.ico'}")


if __name__ == "__main__":
    main()
