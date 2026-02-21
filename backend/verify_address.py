import requests

try:
    response = requests.get("http://localhost:8000/colleges?limit=1000")
    if response.status_code == 200:
        data = response.json()
        lines = []

        # Sample colleges across sheets
        for c in data[:10]:
            lines.append(f"[{c.get('code')}] {c.get('name')[:45]} -> {c.get('location')}")

        lines.append("")

        # Count how many have zone/district names vs college names
        good = 0
        bad = 0
        bad_list = []
        for c in data:
            loc = c.get('location', '')
            name = c.get('name', '')
            if loc == name or loc in name:
                bad += 1
                bad_list.append(f"  BAD: [{c.get('code')}] loc='{loc}' name='{name[:40]}'")
            else:
                good += 1

        lines.append(f"Summary: {good} good, {bad} bad (location = name), total {len(data)}")
        if bad_list:
            lines.append(f"\nBad entries (first 10):")
            for b in bad_list[:10]:
                lines.append(b)

        result = "\n".join(lines)
        print(result)
        with open("verify_results.txt", "w") as f:
            f.write(result)
    else:
        print(f"Error: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
