import requests
import json

try:
    response = requests.get("http://localhost:8000/colleges?limit=2")
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2))
        if len(data) > 0 and "zone" in data[0]:
            print("SUCCESS: Zone field found in response.")
        else:
            print("FAILURE: Zone field NOT found in response.")
    else:
        print(f"FAILURE: Status code {response.status_code}")
except Exception as e:
    print(f"FAILURE: Exception {e}")
