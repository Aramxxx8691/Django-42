#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip

LOG_FILE="path_install.log"

pip install -r requirements.txt > $LOG_FILE 2>&1

if grep -q "ERROR" "$LOG_FILE"; then
    echo "❌ An error occurred during installation. Check $LOG_FILE for details."
    exit 1
else
    echo "✅ Installation successful."
    if [ -n "$VIRTUAL_ENV" ]; then
        if [ -d "d05" ]; then
            cd d05
            echo "📁 Django project already exists."
        else
            django-admin startproject d05
            cd d05
            django-admin startapp ex00
            django-admin startapp ex01
            django-admin startapp ex02
            django-admin startapp ex03 
            echo "📁 Django project created."
        fi
        exec "$SHELL"
    else
        echo "❌ Virtual environment not activated."
        exit 1
    fi
fi
