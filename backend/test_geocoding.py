import requests
import re
import time

def get_coords(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        resp = requests.head(url, allow_redirects=True, timeout=10, headers=headers)
        final_url = resp.url
        print(f"Final URL: {final_url}")
        
        # Extract coords /@lat,lon
        match = re.search(r'/@(-?\d+\.\d+),(-?\d+\.\d+)', final_url)
        if match:
            return match.group(1), match.group(2)
    except Exception as e:
        print(f"Error fetching URL: {e}")
    return None, None

def reverse_geocode(lat, lon):
    try:
        # Nominatim requires User-Agent
        headers = {'User-Agent': 'TNECL-College-App/1.0 (test@example.com)'}
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=14" # Zoom 14 for suburb/city
        
        resp = requests.get(url, headers=headers, timeout=10)
        data = resp.json()
        print(f"Nominatim Data: {data.get('display_name')}")
        return data.get('display_name')
    except Exception as e:
        print(f"Error geocoding: {e}")
        return None

url = "https://maps.app.goo.gl/VGhyu1MkgNSXF5wA6" # College 1102
lat, lon = get_coords(url)
if lat and lon:
    print(f"Coords: {lat}, {lon}")
    time.sleep(1)
    address = reverse_geocode(lat, lon)
    print(f"Address: {address}")
else:
    print("No coords found")
