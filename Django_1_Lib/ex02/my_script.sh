#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip

LOG_FILE="path_install.log"
PROG="request_wikipedia.py"

pip3 install -r requirements.txt > $LOG_FILE 2>&1

if grep -q "ERROR" "$LOG_FILE"; then
    echo "❌ An error occurred during installation. Check $LOG_FILE for details."
else
    echo "✅ Installation successful."
    python3 $PROG "42"
fi

