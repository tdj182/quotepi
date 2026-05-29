# QuotePi

A Raspberry Pi Zero 2 W with a Waveshare 2.13" e-paper display that 
shows themed quotes throughout the day, refreshed automatically via cron.

## What it does

- **5:30am** — Stoic quote (Marcus Aurelius, Seneca, Epictetus)
- **12:00pm** — Motivational quote
- **6:00pm** — Romantic/Poetic quote

Quotes are pulled from a Google Sheet. If the sheet is unreachable, 
falls back to local quotes.json. The display retains the image without 
power between refreshes.

## Hardware

- Raspberry Pi Zero 2 W
- Waveshare 2.13" E-Ink Display HAT V4 (250x122, black/white)
- 64GB SD card
- 5V/2.5A micro-USB power supply

## Software stack

- Raspberry Pi OS Lite (64-bit), headless
- Python 3 + Pillow for rendering
- Waveshare epd2in13_V4 library for display
- Google Sheets CSV as quote source
- cron for scheduling

## Project structure
quotepi/
├── src/
│   ├── quotes_loader.py   # Fetches quotes (Sheets → local fallback)
│   ├── render.py          # Renders quote to PNG
│   ├── display.py         # Sends PNG to e-paper display
│   └── update_quote.py    # Orchestrator — called by cron
├── data/
│   └── quotes.json        # Local fallback quotes
├── output/
│   └── cron.log           # Cron run log
├── run_update.sh          # Cron wrapper script
└── requirements.txt

## Setup

See the full build guide (QuotePi_Build_Guide.docx) for complete 
step-by-step instructions including hardware setup, OS flashing, 
SSH configuration, and display wiring.

Quick dependency install:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Crontab
30 5  * * * /home/tdj182/quotepi/run_update.sh Stoicism
0  12 * * * /home/tdj182/quotepi/run_update.sh Motivational
0  18 * * * /home/tdj182/quotepi/run_update.sh Romantic
@reboot sleep 30 && /home/tdj182/quotepi/run_update.sh Stoicism

## Adding quotes

Edit the Google Sheet directly from any browser or phone — no SSH 
required. New quotes appear at the next scheduled refresh.

To add a new theme:
1. Add rows with the new theme name in the `theme` column of the sheet
2. Add a new line to `data/quotes.json` with the same theme name
3. Add a new cron entry pointing to `run_update.sh YourTheme`

## Manual run

```bash
cd ~/quotepi
source venv/bin/activate
sudo python src/update_quote.py Stoicism
```
