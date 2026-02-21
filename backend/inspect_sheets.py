import json

try:
    with open('official_colleges.json', 'r') as f:
        data = json.load(f)
        
    print(f"Found {len(data)} sheets.")
    for sheet, colleges in data.items():
        if colleges:
            first = colleges[0]
            print(f"{sheet}: Code {first.get('Code')} - {first.get('CollegeName')}")
        else:
            print(f"{sheet}: Empty")
            
except Exception as e:
    print(f"Error: {e}")
