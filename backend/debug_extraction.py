import requests
import urllib.parse

url = "https://maps.app.goo.gl/5nQAwzpipCV6x6pc7"

def resolve_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        resp = requests.head(url, allow_redirects=True, timeout=10, headers=headers)
        print(f"Status Code: {resp.status_code}")
        print(f"Final URL: {resp.url}")
        return resp.url
    except Exception as e:
        print(f"Exception: {e}")
        return None

final_url = resolve_url(url)

if final_url and "/place/" in final_url:
    start = final_url.find("/place/") + 7
    end = final_url.find("/@", start)
    if end == -1: end = len(final_url)
    
    raw_address = final_url[start:end]
    address = urllib.parse.unquote(raw_address).replace("+", " ")
    print(f"Extracted Address: {address}")
else:
    print("Could not extract address.")
