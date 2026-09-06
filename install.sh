```bash
#!/bin/bash

echo "=============================================="
echo "           CyberReconX Installer"
echo "=============================================="

echo "[*] Updating package list..."
sudo apt update

echo "[*] Installing required tools..."

sudo apt install -y \
    python3 \
    nmap \
    whois \
    whatweb \
    ipcalc \
    net-tools

echo ""
echo "[+] Installation completed."
echo "[+] Run the tool with:"
echo ""
echo "    python3 main.py"
echo ""
```
