# PowerShell installer for Windows
Set-StrictMode -Version Latest

Write-Host '=============================================='
Write-Host '           CyberReconX Installer (Windows)' 
Write-Host '=============================================='

Write-Host '[*] Checking for Python...'
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host 'Python not found. Please install Python 3.10+ from https://www.python.org/downloads/' -ForegroundColor Yellow
    exit 1
}

Write-Host '[*] Creating virtual environment (.venv)...'
python -m venv .venv

Write-Host "[*] Activating virtual environment and installing dependencies..."
.
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
if (Test-Path requirements.txt) {
    pip install -r requirements.txt
}

Write-Host '[+] Installation completed.' -ForegroundColor Green
Write-Host 'Run the tool with: .\.venv\Scripts\Activate.ps1; python main.py'

exit 0
