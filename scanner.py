
from urllib.parse import urlparse
import socket

from port_scanner import scan_ports
from header_checker import check_headers
from ssl_checker import check_ssl


def main():

    print("=" * 45)
    print("       VULNERABILITY SCANNER")
    print("=" * 45)

    url = input("Enter target URL (e.g. https://example.com): ")

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed_url = urlparse(url)
    host = parsed_url.hostname

    if not host:
        print("Invalid URL!")
        return

    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        print("Unable to resolve target hostname.")
        return

    report = []

    report.append("VULNERABILITY SCANNER REPORT")
    report.append("=" * 35)
    report.append("Target: " + host)

    # Port Scanning
    port_results = scan_ports(host)
    report.extend(port_results)

    # HTTP Header Checking
    header_results = check_headers(url)
    report.extend(header_results)

    # SSL Checking
    ssl_results = check_ssl(host)
    report.extend(ssl_results)

    # Generate Report
    with open("report.txt", "w") as file:
        file.write("\n".join(report))

    print("\n" + "=" * 45)
    print("SCAN COMPLETED!")
    print("Report saved successfully as report.txt")
    print("=" * 45)


if __name__ == "__main__":
    main()
