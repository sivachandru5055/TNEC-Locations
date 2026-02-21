import requests
import re

url = "https://maps.app.goo.gl/5nQAwzpipCV6x6pc7"

try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    resp = requests.get(url, allow_redirects=True, timeout=10, headers=headers)
    print(f"Status Code: {resp.status_code}")
    
    # Extract Title
    title_match = re.search(r'<title>(.*?)</title>', resp.text)
    if title_match:
        print(f"Title: {title_match.group(1)}")
    
    # Extract og:title
    og_title = re.search(r'<meta property="og:title" content="(.*?)">', resp.text)
    if og_title:
        print(f"OG Title: {og_title.group(1)}")
        
    # Extract og:description (often has address)
    og_desc = re.search(r'<meta property="og:description" content="(.*?)">', resp.text)
    if og_desc:
        print(f"OG Description: {og_desc.group(1)}")

except Exception as e:
    print(f"Exception: {e}")
