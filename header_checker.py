
import requests

def check_headers(url):
    results = []

    print("\nHTTP SECURITY HEADER CHECK")

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        security_headers = [
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Content-Security-Policy",
            "Strict-Transport-Security"
        ]

        for header in security_headers:
            if header in headers:
                status = "PRESENT"
            else:
                status = "MISSING"

            print(f"{header}: {status}")
            results.append(f"{header}: {status}")

        server = headers.get("Server", "Not disclosed")
        print("Server Information:", server)
        results.append("Server Information: " + server)

    except requests.RequestException as e:
        print("Error:", e)
        results.append("HTTP Scan Error: " + str(e))

    return results
