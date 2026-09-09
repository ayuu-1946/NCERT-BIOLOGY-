"""Compose chapter-specific horizontal figure plates for the requested layout."""
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"


def compose_side_by_side(names: list[str], output: str, gap: int = 36) -> None:
    panels = [Image.open(ASSETS / name).convert("L") for name in names]
    target_height = max(im.height for im in panels)
    scaled = []
    for im in panels:
        scale = target_height / im.height
        scaled.append(im.resize((round(im.width * scale), target_height), Image.Resampling.LANCZOS))
    canvas = Image.new("L", (sum(im.width for im in scaled) + gap * (len(scaled) - 1), target_height), 255)
    x = 0
    for im in scaled:
        canvas.paste(im, (x, 0))
        x += im.width + gap
    canvas.save(ASSETS / output, format="PNG", dpi=(300, 300), optimize=True)
    print(output, canvas.size, canvas.mode)


if __name__ == "__main__":
    compose_side_by_side(["fig_5_7.png", "fig_5_8.png"], "fig_5_7_5_8_horizontal.png")
