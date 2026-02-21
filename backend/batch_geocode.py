"""
Batch Address Extractor for All Colleges
-----------------------------------------
Resolves Google Maps short URLs → extracts lat/lon → reverse geocodes via Nominatim.
Saves addresses back to official_colleges.json.

Usage: python batch_geocode.py
"""
import json
import re
import time
import requests

INPUT_FILE = "../official_colleges.json"
OUTPUT_FILE = "../official_colleges.json"  # Overwrite with addresses

HEADERS = {
    "User-Agent": "TNECL-College-App/1.0 (college-address-extraction)"
}

GMAPS_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def resolve_gmaps_url(short_url):
    """Resolve a Google Maps short URL and extract lat/lon coordinates."""
    try:
        resp = requests.head(short_url, allow_redirects=True, timeout=10, headers=GMAPS_HEADERS)
        final_url = resp.url

        # Try /@lat,lon pattern
        match = re.search(r'/@(-?\d+\.\d+),(-?\d+\.\d+)', final_url)
        if match:
            return float(match.group(1)), float(match.group(2))

        # Try ?q=lat,lon or !3d lat !4d lon patterns
        match = re.search(r'!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)', final_url)
        if match:
            return float(match.group(1)), float(match.group(2))

    except Exception as e:
        print(f"    URL resolve error: {e}")
    return None, None


def reverse_geocode(lat, lon):
    """Reverse geocode lat/lon via Nominatim to get a human-readable address."""
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=16&addressdetails=1"
        resp = requests.get(url, headers=HEADERS, timeout=10)

        if resp.status_code == 200:
            data = resp.json()
            # Build a concise address from address components
            addr = data.get("address", {})

            # Build address parts
            parts = []

            # Suburb/village/neighbourhood
            for key in ["suburb", "village", "neighbourhood", "hamlet"]:
                if key in addr:
                    parts.append(addr[key])
                    break

            # City/town
            for key in ["city", "town", "city_district"]:
                if key in addr:
                    parts.append(addr[key])
                    break

            # State
            if "state" in addr:
                parts.append(addr["state"])

            # Postcode
            if "postcode" in addr:
                parts[-1] = parts[-1] + " " + addr["postcode"] if parts else addr["postcode"]

            # Country
            if "country" in addr:
                parts.append(addr["country"])

            if parts:
                return ", ".join(parts)
            else:
                return data.get("display_name", "")
        else:
            print(f"    Nominatim HTTP {resp.status_code}")
    except Exception as e:
        print(f"    Geocode error: {e}")
    return None


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    total = 0
    success = 0
    skipped = 0
    failed = 0

    for sheet_name, colleges in data.items():
        total += len(colleges)

    print(f"Total colleges: {total}")
    print(f"Starting batch geocoding...\n")

    count = 0
    for sheet_name, colleges in data.items():
        for item in colleges:
            count += 1
            name = item.get("CollegeName", "N/A")
            code = item.get("Code", "")
            map_link = item.get("Location", "")

            # Skip if Address already exists
            if item.get("Address", "").strip():
                skipped += 1
                print(f"[{count}/{total}] [{code}] SKIP (already has address)")
                continue

            if not map_link or "goo.gl" not in map_link:
                failed += 1
                print(f"[{count}/{total}] [{code}] FAIL (no Google Maps URL)")
                continue

            print(f"[{count}/{total}] [{code}] {name[:50]}...", end=" ")

            # Step 1: Resolve URL to get coordinates
            lat, lon = resolve_gmaps_url(map_link)
            if lat is None:
                failed += 1
                print("FAIL (no coords)")
                time.sleep(0.5)
                continue

            # Step 2: Reverse geocode
            time.sleep(1.1)  # Nominatim rate limit: 1 request/second
            address = reverse_geocode(lat, lon)

            if address:
                item["Address"] = address
                success += 1
                print(f"-> {address}")
            else:
                failed += 1
                print("FAIL (geocode failed)")

            # Save progress every 25 colleges
            if count % 25 == 0:
                with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  [Progress saved: {success} success, {failed} failed, {skipped} skipped]")

    # Final save
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"DONE!")
    print(f"  Total:   {total}")
    print(f"  Success: {success}")
    print(f"  Skipped: {skipped} (already had address)")
    print(f"  Failed:  {failed}")
    print(f"\nAddresses saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
