```python
#!/usr/bin/env python3

import subprocess
import re
import sys


def banner():
    print("=" * 60)
    print("                    CYBERRECONX")
    print("                NETWORK RECON TOOLKIT")
    print("=" * 60)


def check_tool(tool):
    result = subprocess.run(
        ["which", tool],
        capture_output=True,
        text=True
    )

    return result.returncode == 0


def run_command(command):
    try:
        return subprocess.run(
            command,
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        return None


def local_network_recon():
    print("\n[*] Fetching local network configuration...")

    if not check_tool("ifconfig"):
        print("[-] Error: ifconfig is not installed.")
        print("[!] Run: sudo apt install net-tools")
        return

    if not check_tool("ipcalc"):
        print("[-] Error: ipcalc is not installed.")
        print("[!] Run: sudo apt install ipcalc")
        return

    result = run_command(["ifconfig"])

    if result is None or result.returncode != 0:
        print("[-] Error: Could not run ifconfig.")
        return

    ip_matches = re.findall(
        r"inet (\d+\.\d+\.\d+\.\d+)",
        result.stdout
    )

    mask_matches = re.findall(
        r"netmask (\d+\.\d+\.\d+\.\d+)",
        result.stdout
    )

    ip_address = None

    for ip in ip_matches:
        if ip != "127.0.0.1":
            ip_address = ip
            break

    if ip_address is None or not mask_matches:
        print("[-] Error: Could not find local network information.")
        return

    subnet_mask = mask_matches[0]

    print(f"[+] Local IP Address : {ip_address}")
    print(f"[+] Local Subnet Mask: {subnet_mask}")

    print("\n[*] Calculating network range...")

    result = run_command(
        ["ipcalc", f"{ip_address}/{subnet_mask}"]
    )

    if result is None or result.returncode != 0:
        print("[-] Error: ipcalc failed.")
        return

    match = re.search(
        r"Network:\s+(\d+\.\d+\.\d+\.\d+)/(\d+)",
        result.stdout
    )

    if not match:
        print("[-] Error: Could not calculate network range.")
        return

    network_address = match.group(1)
    prefix_length = match.group(2)

    target_range = f"{network_address}/{prefix_length}"

    print(f"[+] Target Network   : {target_range}")

    nmap_scan(target_range)


def custom_network_recon():
    target = input(
        "\n[?] Enter IP or network range "
        "(example: 192.168.1.0/24): "
    ).strip()

    if not target:
        print("[-] Target cannot be empty.")
        return

    print(f"[+] Target set to: {target}")

    nmap_scan(target)


def nmap_scan(target):
    if not check_tool("nmap"):
        print("[-] Error: Nmap is not installed.")
        print("[!] Run: sudo apt install nmap")
        return

    print("\n[+] Select Nmap Scan Type:")
    print("    1. Standard Service Scan")
    print("    2. Aggressive Scan")
    print("    3. OS Detection")
    print("    4. Back")

    choice = input("\n[?] Enter your choice: ").strip()

    if choice == "1":
        nmap_args = ["-sV", "-sC"]
        print("\n[*] Running standard Nmap scan...")

    elif choice == "2":
        nmap_args = ["-A"]
        print("\n[*] Running aggressive Nmap scan...")

    elif choice == "3":
        nmap_args = ["-O"]
        print("\n[*] Running OS detection scan...")

    elif choice == "4":
        return

    else:
        print("[-] Invalid scan option.")
        return

    command = ["nmap"] + nmap_args + [target]

    print("\n[*] Scan started...\n")

    result = run_command(command)

    if result is None:
        print("[-] Error: Could not execute Nmap.")
        return

    print("-" * 60)
    print("                    NMAP RESULTS")
    print("-" * 60)

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


def osint_scan():
    target = input(
        "\n[?] Enter target domain or IP "
        "(example: example.com): "
    ).strip()

    if not target:
        print("[-] Target cannot be empty.")
        return

    if not check_tool("whois"):
        print("[-] Error: Whois is not installed.")
        print("[!] Run: sudo apt install whois")
        return

    if not check_tool("whatweb"):
        print("[-] Error: WhatWeb is not installed.")
        print("[!] Run: sudo apt install whatweb")
        return

    print(f"\n[*] Running Whois on: {target}")

    whois_result = run_command(
        ["whois", target]
    )

    if whois_result is not None:
        print("\n" + "-" * 60)
        print("                    WHOIS RESULTS")
        print("-" * 60)

        lines = whois_result.stdout.splitlines()

        for line in lines[:20]:
            print(line)

    print(f"\n[*] Running WhatWeb on: {target}")

    whatweb_result = run_command(
        ["whatweb", target]
    )

    if whatweb_result is not None:
        print("\n" + "-" * 60)
        print("                   WHATWEB RESULTS")
        print("-" * 60)

        print(whatweb_result.stdout)

    print("\n[*] OSINT operation completed.")


def main():
    while True:
        banner()

        print("\n[+] Select an option:")
        print("    1. Local Network Recon")
        print("    2. Custom Network Recon")
        print("    3. OSINT & Technology Fingerprinting")
        print("    4. Exit")

        choice = input("\n[?] Enter your choice: ").strip()

        if choice == "1":
            local_network_recon()

        elif choice == "2":
            custom_network_recon()

        elif choice == "3":
            osint_scan()

        elif choice == "4":
            print("\n[*] Exiting CyberReconX.")
            sys.exit(0)

        else:
            print("\n[-] Invalid option.")

        input("\n[Press Enter to return to the main menu]")


if __name__ == "__main__":
    main()
```
