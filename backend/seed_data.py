import asyncio
from database import db
from auth import get_password_hash

async def seed_data():
    # Clear existing data
    await db["colleges"].delete_many({})
    await db["users"].delete_many({})
    
    # Create a test user
    test_user = {
        "email": "test@example.com",
        "hashed_password": get_password_hash("password123"),
        "disabled": False
    }
    await db["users"].insert_one(test_user)
    
    # Sample colleges based on user data
    colleges = [
        {
            "name": "IIT Madras",
            "location": "Chennai",
            "type": "Government",
            "affiliated_to": "Independent",
            "fees_btech": 200000,
            "fees_mtech": 75000,
            "avg_package": 1500000,
            "latitude": 12.9915,
            "longitude": 80.2336
        },
        {
            "name": "NIT Trichy",
            "location": "Tiruchirappalli",
            "type": "Government",
            "affiliated_to": "Independent",
            "fees_btech": 150000,
            "fees_mtech": 60000,
            "avg_package": 1200000,
            "latitude": 10.7589,
            "longitude": 78.8132
        },
        {
            "name": "VIT Vellore",
            "location": "Vellore",
            "type": "Private",
            "affiliated_to": "Deemed University",
            "fees_btech": 198000,
            "fees_mtech": 80000,
            "avg_package": 900000,
            "latitude": 12.9717,
            "longitude": 79.1588
        },
        {
            "name": "CEG Anna University",
            "location": "Chennai",
            "type": "Government",
            "affiliated_to": "Anna University",
            "fees_btech": 50000,
            "fees_mtech": 30000,
            "avg_package": 1000000,
            "latitude": 13.0131,
            "longitude": 80.2364
        },
        {
            "name": "PSG College of Technology",
            "location": "Coimbatore",
            "type": "Private",
            "affiliated_to": "Anna University",
            "fees_btech": 250000,
            "fees_mtech": 90000,
            "avg_package": 850000,
            "latitude": 11.0247,
            "longitude": 76.9939
        }
    ]
    
    # Add more generic colleges to represent the ~959 colleges
    for i in range(10):
        colleges.append({
            "name": f"Generic Engineering College {i+1}",
            "location": "Tamil Nadu",
            "type": "Private" if i % 6 != 0 else "Government",
            "affiliated_to": "Anna University",
            "fees_btech": 150000 + (i * 1000),
            "fees_mtech": 60000 + (i * 500),
            "avg_package": 700000 + (i * 10000),
            "latitude": 11.0 + (i * 0.1),
            "longitude": 78.0 + (i * 0.1)
        })

    await db["colleges"].insert_many(colleges)
    print("Database seeded successfully!")

if __name__ == "__main__":
    asyncio.run(seed_data())
