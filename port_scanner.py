
import socket

def scan_ports(target):
    ports = [21, 22, 80, 443, 3306, 8080]

    results = []

    print("\nPORT SCANNING")

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSED"

        print(f"Port {port}: {status}")
        results.append(f"Port {port}: {status}")

        s.close()

    return results
