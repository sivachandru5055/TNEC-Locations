import requests

url = "https://maps.app.goo.gl/5nQAwzpipCV6x6pc7"
try:
    resp = requests.head(url, allow_redirects=True)
    print(f"Final URL: {resp.url}")
except Exception as e:
    print(f"Error: {e}")
