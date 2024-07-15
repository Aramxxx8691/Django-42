#!/bin/bash
echo "❇️  Using piprsion: $(pip3 --version)"
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
echo "❇️  Using piprsion: $(pip3 --version)"

LIB_DIR="local_lib"
LOG_FILE="path_install.log"
GIT_REPO="git+https://github.com/jaraco/path.git"

if [ -d $LIB_DIR ]; then
    echo "♨️  Deleting $LIB_DIR"
    rm -rf $LIB_DIR
fi

mkdir -p "$LIB_DIR"

echo "♻️  Installing path.py from GitHub..."
pip3 install "$GIT_REPO" -t "$LIB_DIR" &> "$LOG_FILE"

if grep -q "ERROR" "$LOG_FILE"; then
    echo "❌ An error occurred during installation. Check $LOG_FILE for details."
else
    echo "✅ Installation successful."
    python3 my_program.py
fi

