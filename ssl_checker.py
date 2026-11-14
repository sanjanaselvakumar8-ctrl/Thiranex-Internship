
import socket
import ssl
from datetime import datetime

def check_ssl(host):
    results = []

    print("\nSSL CERTIFICATE CHECK")

    try:
        context = ssl.create_default_context()

        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as secure_sock:

                certificate = secure_sock.getpeercert()

                expiry = certificate.get("notAfter")

                if expiry:
                    expiry_date = datetime.strptime(
                        expiry, "%b %d %H:%M:%S %Y %Z"
                    )

                    if expiry_date > datetime.utcnow():
                        status = "VALID"
                    else:
                        status = "EXPIRED"

                    print("Certificate:", status)
                    print("Expiry Date:", expiry_date)

                    results.append("SSL Certificate: " + status)
                    results.append("Expiry Date: " + str(expiry_date))

    except Exception as e:
        print("SSL Error:", e)
        results.append("SSL Error: " + str(e))

    return results
