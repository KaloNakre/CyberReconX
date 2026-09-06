# CyberReconX

CyberReconX is a small reconnaissance helper tool. The following instructions show how to install and run it on Kali Linux.

## Requirements

- Python 3.10+ (or the system default `python3`)
- pip (`pip3`)
- git

## Install on Kali Linux

1. Update apt and install system packages:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git build-essential libssl-dev libffi-dev
```

2. Clone the repository (or use the files in this folder):

```bash
git clone https://github.com/KaloNakre/CyberReconX.git
cd CyberReconX
```

3. (Recommended) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install Python dependencies from `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

5. Run the tool:

```bash
python3 main.py
```

If the tool requires elevated privileges for certain network operations, run it with `sudo` only when necessary and after understanding the implications.

## Notes

- If you prefer using a system-wide install, omit the virtual environment steps and use `pip3` instead of `pip`.
- If any dependencies fail to build (native extensions), ensure `build-essential`, `libssl-dev`, and `libffi-dev` are installed.

If you'd like, I can also add a separate `INSTALL-KALI.md` with step-by-step screenshots or create a small install script.