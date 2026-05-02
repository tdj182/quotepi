"""Load and select quotes from the JSON file."""
import json
import random
from pathlib import Path

QUOTES_PATH = Path(__file__).parent.parent / "data" / "quotes.json"


def load_quotes():
    with open(QUOTES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def random_quote():
    quotes = load_quotes()
    return random.choice(quotes)


if __name__ == "__main__":
    print(random_quote())
