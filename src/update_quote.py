"""Pick a themed quote, render it, push to the display."""
import sys
from quotes_loader import random_quote
from render import render_quote
from display import show_image

# Theme passed as command-line argument, defaults to Stoicism
THEME = sys.argv[1] if len(sys.argv) > 1 else "Stoicism"


def main():
    q = random_quote(THEME)
    path = render_quote(q["text"], q["author"])
    show_image(path)
    print(f"[{THEME}] Displayed: {q['author']}")


if __name__ == "__main__":
    main()
