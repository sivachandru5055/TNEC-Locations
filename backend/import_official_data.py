import asyncio
import json
import random
from database import db
from models import CollegeCreate

async def import_colleges():
    try:
        # Read from root directory
        with open('../official_colleges.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("official_colleges.json not found!")
        return

    # City Mapping for better coordinates and locations
    CITY_COORDS = {
        "Chennai": (13.0827, 80.2707),
        "Coimbatore": (11.0168, 76.9558),
        "Madurai": (9.9252, 78.1198),
        "Trichy": (10.7905, 78.7047),
        "Tiruchirappalli": (10.7905, 78.7047),
        "Salem": (11.6643, 78.1460),
        "Tirunelveli": (8.7139, 77.7567),
        "Vellore": (12.9165, 79.1325),
        "Erode": (11.3410, 77.7172),
        "Thanjavur": (10.7870, 79.1378),
        "Tiruppur": (11.1085, 77.3411),
        "Kanchipuram": (12.8342, 79.7036),
        "Thiruvallur": (13.1394, 79.9073),
        "Namakkal": (11.2189, 78.1672),
        "Dindigul": (10.3673, 77.9803),
        "Hosur": (12.7409, 77.8253),
        "Virudhunagar": (9.5872, 77.9514),
        "Sivakasi": (9.4533, 77.8024),
        "Karaikudi": (10.0747, 78.7845),
        "Pollachi": (10.6593, 77.0101),
        "Karur": (10.9601, 78.0766),
        "Nagapattinam": (10.7672, 79.8449),
        "Ramanathapuram": (9.3639, 78.8395),
        "Thiruvarur": (10.7661, 79.6433),
        "Theni": (10.0104, 77.4768),
        "Dharmapuri": (12.1271, 78.1582),
        "Krishnagiri": (12.5186, 78.2138),
        "Villupuram": (11.9401, 79.4861),
        "Viluppuram": (11.9401, 79.4861),
        "Cuddalore": (11.7480, 79.7714),
        "Perambalur": (11.2342, 78.8817),
        "Ariyalur": (11.1390, 79.0735),
        "Pudukkottai": (10.3797, 78.8202),
        "Sivaganga": (9.8433, 78.4833),
        "Tenkasi": (8.9591, 77.3144),
        "Tirupathur": (12.4935, 78.5678),
        "Ranipet": (12.9272, 79.3333),
        "Kallakurichi": (11.7377, 78.9622),
        "Chengalpattu": (12.6841, 79.9836),
        "Kanyakumari": (8.0883, 77.5385),
        "Nagercoil": (8.1833, 77.4119),
        "Avadi": (13.1067, 80.1099),
        "Ambattur": (13.0982, 80.1620),
        "Tambaram": (12.9249, 80.1000),
        "Poonamallee": (13.0382, 80.0962),
        "Sriperumbudur": (12.9675, 79.9428),
        "Chromepet": (12.9516, 80.1462),
        "Guduvancheri": (12.8477, 80.0614),
        "Tindivanam": (12.2340, 79.6567),
        "Gummidipoondi": (13.4050, 80.1078),
    }

    # Sheet-to-district mapping
    SHEET_LOCATIONS = {
        "Sheet1": "Thiruvallur",
        "Sheet2": "Kanchipuram",
        "Sheet3": "Chennai",
        "Sheet4": "Villupuram",
        "Sheet5": "Tindivanam",
        "Sheet6": "Vellore",
        "Sheet7": "Salem",
        "Sheet8": "Trichy",
        "Sheet9": "Madurai",
    }

    # Flatten sheets
    all_colleges = []
    for sheet_name, colleges in data.items():
        for item in colleges:
            name = item.get("CollegeName", "N/A")
            code = str(item.get("Code", ""))
            website = item.get("Website", "")
            map_link = item.get("Location", "")

            is_govt = any(x in name for x in ["Govt", "Government", "University"])
            college_type = "Government" if is_govt else "Private"

            # Priority 1: Manual "Address" field in JSON (most specific)
            manual_address = item.get("Address", "").strip()

            # Default: Sheet/zone mapping
            location_name = SHEET_LOCATIONS.get(sheet_name, "Tamil Nadu")
            lat, lon = 11.0 + random.uniform(-2, 2), 78.0 + random.uniform(-1, 2)

            if manual_address:
                # Use explicit address from JSON
                location_name = manual_address
            else:
                # Try to extract city from college name
                found_city = None
                for city in CITY_COORDS:
                    if city.lower() in name.lower():
                        found_city = city
                        break

                if found_city:
                    location_name = found_city
                    base_lat, base_lon = CITY_COORDS[found_city]
                    lat = base_lat + random.uniform(-0.1, 0.1)
                    lon = base_lon + random.uniform(-0.1, 0.1)
                elif "," in name:
                    # Use text after last comma only if it looks like a city
                    candidate = name.split(",")[-1].strip()
                    # Check if the candidate matches a known city
                    for city in CITY_COORDS:
                        if city.lower() in candidate.lower():
                            location_name = city
                            base_lat, base_lon = CITY_COORDS[city]
                            lat = base_lat + random.uniform(-0.1, 0.1)
                            lon = base_lon + random.uniform(-0.1, 0.1)
                            break

            college = {
                "name": name,
                "code": code,
                "website": website,
                "location": location_name,
                "type": college_type,
                "affiliated_to": "Anna University" if not is_govt else "Independent",
                "fees_btech": random.choice([50000, 85000, 150000, 250000]),
                "fees_mtech": random.choice([30000, 60000, 90000]),
                "avg_package": random.randint(400000, 1200000),
                "latitude": lat,
                "longitude": lon,
                "location_url": map_link
            }
            all_colleges.append(college)

    if all_colleges:
        await db["colleges"].delete_many({})  # Clear old data
        await db["colleges"].insert_many(all_colleges)
        print(f"Successfully imported {len(all_colleges)} colleges!")
    else:
        print("No colleges found in JSON.")

if __name__ == "__main__":
    asyncio.run(import_colleges())
