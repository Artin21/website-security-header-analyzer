import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scanner.headers_check import analyze_headers

def test_google():
    url = "https://www.google.com"
    result = analyze_headers(url)
    assert "rating" in result
    print(f"[Google] Rating: {result['rating']}")

def test_example():
    url = "https://example.com"
    result = analyze_headers(url)
    assert "rating" in result
    print(f"[Example.com] Rating: {result['rating']}")

def test_neverssl():
    url = "http://neverssl.com"
    result = analyze_headers(url)
    assert "rating" in result
    print(f"[NeverSSL] Rating: {result['rating']}")

if __name__ == "__main__":
    print("Kör tester..")
    test_google()
    test_example()
    test_neverssl()
    print("Tester klara!") 
