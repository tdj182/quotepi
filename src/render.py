"""Render a quote to a PNG sized for the 2.13\" e-paper display."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

from quotes_loader import random_quote

WIDTH, HEIGHT = 250, 122
OUTPUT_PATH = Path(__file__).parent.parent / "output" / "current.png"

FONT_QUOTE = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_AUTHOR = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"


def render_quote(quote_text, author):
    img = Image.new("1", (WIDTH, HEIGHT), 1)  # 1 = white in mode "1"
    draw = ImageDraw.Draw(img)

    for size in (16, 14, 12, 11, 10):
        font = ImageFont.truetype(FONT_QUOTE, size)
        avg_char_w = font.getlength("abcdefghijklmnopqrstuvwxyz") / 26
        chars_per_line = int((WIDTH - 16) / avg_char_w)
        wrapped = textwrap.wrap(quote_text, width=chars_per_line)
        line_h = size + 2
        total_h = line_h * len(wrapped) + size + 8
        if total_h <= HEIGHT - 8:
            break

    y = 6
    for line in wrapped:
        draw.text((8, y), line, font=font, fill=0)  # 0 = black in mode "1"
        y += line_h

    author_font = ImageFont.truetype(FONT_AUTHOR, max(size - 2, 9))
    author_text = f"\u2014 {author}"
    aw = author_font.getlength(author_text)
    draw.text((WIDTH - aw - 8, HEIGHT - (size - 2) - 8),
              author_text, font=author_font, fill=0)

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    img.save(OUTPUT_PATH)
    return OUTPUT_PATH


if __name__ == "__main__":
    q = random_quote()
    path = render_quote(q["text"], q["author"])
    print(f"Rendered to {path}")
