"""Send the rendered quote PNG to the Waveshare 2.13" V4 e-paper display."""
import sys
from pathlib import Path
from PIL import Image

from waveshare_epd import epd2in13_V4

IMAGE_PATH = Path(__file__).parent.parent / "output" / "current.png"


def show_image(path):
    epd = epd2in13_V4.EPD()
    epd.init()
    epd.Clear(0xFF)

    img = Image.open(path)

    if img.size == (250, 122):
        img = img.rotate(90, expand=True)

    if img.mode != "1":
        img = img.convert("1")

    epd.display(epd.getbuffer(img))
    epd.sleep()


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else IMAGE_PATH
    show_image(path)
    print(f"Displayed {path}")
