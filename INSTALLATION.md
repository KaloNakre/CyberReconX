# Installation Guide

This guide covers easy, one-command installation for common environments so anyone can get `CyberReconX` running quickly.

## Quick (All Platforms)

1. Clone the repo:

```bash
git clone https://github.com/KaloNakre/CyberReconX.git
cd CyberReconX
```

2. Run the platform installer below.

---

## Kali / Debian / Ubuntu

Run the included `install.sh` which installs system packages and shows next steps:

```bash
sudo bash install.sh
# then
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 main.py
```

## Windows (PowerShell)

Open PowerShell as Administrator (if you need to install system packages). Then run:

```powershell
.\install.ps1
# then
.\.venv\Scripts\Activate.ps1
python main.py
```

## Installing Python dependencies

If `requirements.txt` contains packages, the installers will call `pip install -r requirements.txt`.

To add new Python dependencies, update `requirements.txt` with one package per line, then commit.

## Notes & Troubleshooting

- If you see permission errors on Linux, rerun with `sudo` for the system package installs only.
- For network or raw-socket operations, elevated privileges may be required.
- If a dependency fails to build, ensure `build-essential`, `libssl-dev`, and `libffi-dev` are installed on Debian-based systems.

If you want, I can also add a single `setup.py` or `pyproject.toml` to make installation via `pip install .` possible. Tell me which you'd prefer.
