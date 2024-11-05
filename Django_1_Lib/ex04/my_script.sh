#!/bin/bash
python3 -m venv django_venv
source django_venv/bin/activate
pip3 install --upgrade pip

LOG_FILE="path_install.log"

pip install -r requirements.txt > $LOG_FILE 2>&1

if grep -q "ERROR" "$LOG_FILE"; then
    echo "❌ An error occurred during installation. Check $LOG_FILE for details."
else
    echo "✅ Installation successful."
    exec "$SHELL"
fi
