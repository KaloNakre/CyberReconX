````markdown
# CyberReconX

CyberReconX is a simple Linux command-line network reconnaissance toolkit.

It uses Python to automate common Linux cybersecurity tools such as Nmap, Whois, WhatWeb, ifconfig, and ipcalc.

## Features

- Local Network Recon
- Custom Network Recon
- Nmap Service Scanning
- Nmap Aggressive Scanning
- Nmap OS Detection
- Whois OSINT
- WhatWeb Technology Fingerprinting

## Tools Used

| Tool | Purpose |
|------|---------|
| Python | Main controller |
| ifconfig | Network information |
| ipcalc | Network calculation |
| Nmap | Network reconnaissance |
| Whois | Domain/IP information |
| WhatWeb | Technology fingerprinting |

## Requirements

- Linux / Kali Linux
- Python 3
- Nmap
- Whois
- WhatWeb
- ipcalc
- net-tools

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
````

Enter the project directory:

```bash
cd CyberReconX
```

Make the installer executable:

```bash
chmod +x install.sh
```

Run the installer:

```bash
./install.sh
```

## Run

Start CyberReconX with:

```bash
python3 main.py
```

## One-Command Installation

After replacing `YOUR_GITHUB_REPOSITORY_URL` with the real repository URL:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL && cd CyberReconX && chmod +x install.sh && ./install.sh
```

## Manual Dependency Installation

If you want to install the dependencies manually:

```bash
sudo apt update
```

```bash
sudo apt install -y python3 nmap whois whatweb ipcalc net-tools
```

Then run:

```bash
python3 main.py
```

## Usage

After starting the program, the following menu is displayed:

```text
1. Local Network Recon
2. Custom Network Recon
3. OSINT & Technology Fingerprinting
4. Exit
```

### 1. Local Network Recon

The program detects the local IP address and subnet mask using `ifconfig`.

Then `ipcalc` calculates the network range.

Finally, the user can select an Nmap scan.

### 2. Custom Network Recon

The user manually enters an IP address or network range.

Example:

```text
192.168.1.0/24
```

The user can then select an Nmap scan type.

### 3. OSINT & Technology Fingerprinting

The user enters a domain or IP address.

CyberReconX uses:

* Whois
* WhatWeb

to display basic OSINT and technology information.

## Nmap Scan Types

### Standard Service Scan

```bash
nmap -sV -sC TARGET
```

### Aggressive Scan

```bash
nmap -A TARGET
```

### OS Detection

```bash
nmap -O TARGET
```

## Project Structure

```text
CyberReconX/
├── main.py
├── install.sh
├── requirements.txt
├── README.md
└── LICENSE
```

## Workflow

### Local Network Recon

```text
ifconfig
    ↓
IP Address
    ↓
Subnet Mask
    ↓
ipcalc
    ↓
Network Range
    ↓
Nmap
    ↓
Results
```

### Custom Network Recon

```text
User Input
    ↓
Target IP / Network
    ↓
Nmap
    ↓
Results
```

### OSINT

```text
Target
    ↓
Whois
    ↓
WhatWeb
    ↓
Results
```

## How It Works

CyberReconX uses Python's `subprocess` module to execute Linux cybersecurity tools.

The basic architecture is:

```text
Python
   ↓
subprocess
   ↓
Linux Tools
   ↓
Reconnaissance Results
```

## Safety Notice

This project is intended for educational and authorized security testing only.

Only scan networks, systems, and websites that you own or have explicit permission to test.

```
```
