#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip

LOG_FILE="path_install.log"

pip3 install django==3.2.3 > $LOG_FILE 2>&1

if grep -q "ERROR" "$LOG_FILE"; then
    echo "❌ An error occurred during installation. Check $LOG_FILE for details."
    exit 1
else
    echo "✅ Installation successful."
    if [ -n "$VIRTUAL_ENV" ]; then
        if [ -d "d09" ]; then
            cd d09
            echo "📁 Django project already exists."
        else
            django-admin startproject d09
            cd d09
            django-admin startapp account
            django-admin startapp chat

            echo "📁 Django project created."
        fi
        exec "$SHELL"
    else
        echo "❌ Virtual environment not activated."
        exit 1
    fi
fi
