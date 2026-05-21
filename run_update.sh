#!/bin/bash
# Wrapper for cron. Accepts theme as first argument.
# Usage: run_update.sh Stoicism
cd /home/tdj182/quotepi
source venv/bin/activate
sudo python src/update_quote.py "$1" >> /home/tdj182/quotepi/output/cron.log 2>&1
