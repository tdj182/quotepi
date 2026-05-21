"""Load quotes by theme — Google Sheets first, local JSON fallback."""
import json
import random
import urllib.request
from pathlib import Path

SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRqDhvnr7VMeT1a7071oCTjynyXaYbooL7xrFqiRBcqzm4WJUg-JrRm3_6wTBd8vScaQDEEbeAW6kae/pub?gid=0&single=true&output=csv"
QUOTES_PATH = Path(__file__).parent.parent / "data" / "quotes.json"


def fetch_from_sheet(theme):
    """Fetch quotes from Google Sheets CSV, filter by theme."""
    try:
        import csv
        import io

        with urllib.request.urlopen(SHEET_URL, timeout=10) as response:
            raw = response.read().decode("utf-8")

        reader = csv.DictReader(io.StringIO(raw))
        quotes = []
        for row in reader:
            if row["theme"].strip().lower() == theme.lower():
                quotes.append({
                    "theme":  row["theme"].strip(),
                    "text":   row["text"].strip(),
                    "author": row["author"].strip(),
                })

        if quotes:
            print(f"[sheets] Loaded {len(quotes)} {theme} quotes")
            return quotes

    except Exception as e:
        print(f"[sheets] Failed: {e}")

    return None

def fetch_from_local(theme):
    """Load quotes from local JSON fallback, filter by theme."""
    with open(QUOTES_PATH, "r", encoding="utf-8") as f:
        all_quotes = json.load(f)
    quotes = [q for q in all_quotes if q["theme"].lower() == theme.lower()]
    print(f"[local] Loaded {len(quotes)} {theme} quotes")
    return quotes


def random_quote(theme):
    """Return a random quote for the given theme."""
    quotes = fetch_from_sheet(theme) or fetch_from_local(theme)
    if not quotes:
        raise ValueError(f"No quotes found for theme: {theme}")
    return random.choice(quotes)


if __name__ == "__main__":
    import sys
    theme = sys.argv[1] if len(sys.argv) > 1 else "Stoicism"
    print(random_quote(theme))
