import requests

SECURITY_HEADERS = {
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
}

def analyze_headers(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        present = {}
        missing = []

        for header in SECURITY_HEADERS:
            if header in headers:
                present[header] = headers[header]
            else:
                missing.append(header)

        # Klassificering
        if len(missing) == 0:
            rating = "Säker"
        elif len(missing) <= 2:
            rating = "Varning"
        else:
            rating = "Osäker"

        # Poängberäkning
        total = len(SECURITY_HEADERS)
        found = len(present)
        percentage = round((found / total) * 100)

        return {
            "status_code": response.status_code,
            "present_headers": present,
            "missing_headers": missing,
            "rating": rating,
            "score_percent": percentage
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e),
            "present_headers": {},
            "missing_headers": list(SECURITY_HEADERS),
            "rating": "Osäker",
            "score_percent": 0
        }
