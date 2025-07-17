import socket
import os

def scan_ports(target, ports, timeout=2):
    print(f"\nScanning {target} on {len(ports)} ports (timeout={timeout}s)\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            try:
                error_msg = os.strerror(result)
            except ValueError:
                error_msg = "Unknown error"
            print(f"[-] Port {port} is closed or filtred (Error code {result}: {error_msg})")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP adress: ")

    print("🔧 Scan mode:")
    print("  [1] Ports 1 to 1024")
    print("  [2] Custom ports (ex: 22,80,443)")
    print("  [3] Full scan (1 to 65535) 🧨💣💥")

    mode = input("Select scan mode (1/2/3): ")

    if mode == "1":
        ports_to_scan = list(range(1, 1025))
    elif mode == "2":
        port_input = input("Enter ports to scan (comma separated): ")
        try:
            ports_to_scan = [int(p.strip()) for p in port_input.split(',')]
        except ValueError:
            print("Invalide ports list")
            exit(1)
    elif mode == "3":
        ports_to_scan = list(range(1, 65536))
    else:
        print("Invalid mode")
        exit(1)

    timeout_input = input("⏱️  Enter timeout in seconds (default = 2): ").strip()

    if timeout_input == "":
            timeout_value = 2
    else:
            try:
                timeout_value = float(timeout_input)
            except ValueError:
                print("⛔ Timeout must be a number like 1.5 or 3")
                exit(1)

    scan_ports(target_ip, ports_to_scan, timeout=timeout_value)
