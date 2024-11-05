#!/bin/bash
echo "❇️  Using pip version: $(pip3 --version)"
source $VIRTUAL_ENV/bin/activate

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
    exec "$SHELL"
fi
