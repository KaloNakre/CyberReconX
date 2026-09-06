#!/bin/bash

set -euo pipefail

echo "=============================================="
echo "           CyberReconX Installer"
echo "=============================================="

echo "[*] Updating package list..."
sudo apt update

echo "[*] Installing required tools..."

sudo apt install -y \
    python3 \
    python3-venv \
    python3-pip \
    nmap \
    whois \
    whatweb \
    ipcalc \
    net-tools

echo ""
echo "[+] Installation completed."
echo "[+] Next steps:"
echo " 1) Create a virtualenv: python3 -m venv .venv"
echo " 2) Activate it: source .venv/bin/activate"
echo " 3) Install Python deps (if any): pip install -r requirements.txt"
echo " 4) Run: python3 main.py"
echo ""
echo "Note: Run this script with sudo only when prompted."

exit 0
