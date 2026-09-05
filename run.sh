#!/bin/bash

if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Please install pip first."
    exit 1
fi

pip install -r requirements.txt
# pip install -r requirements.txt --break-system-packages

cd src/
python3 main.py
