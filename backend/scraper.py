import asyncio
from database import db
from datetime import datetime
import random

async def update_college_fees():
    """
    Simulates fetching updated fees from an external source (e.g., TNEA official announcement).
    In a real scenario, this would use httpx or BeautifulSoup to scrape official PDFs or websites.
    """
    colleges = await db["colleges"].find().to_list(1000)
    updated_count = 0
    
    for college in colleges:
        # Simulate a 2-5% increase in fees as per academic year updates
        increase_percent = random.uniform(1.02, 1.05)
        new_btech_fee = int(college["fees_btech"] * increase_percent)
        new_mtech_fee = int(college["fees_mtech"] * increase_percent)
        
        await db["colleges"].update_one(
            {"_id": college["_id"]},
            {
                "$set": {
                    "fees_btech": new_btech_fee,
                    "fees_mtech": new_mtech_fee,
                    "last_updated": datetime.utcnow()
                }
            }
        )
        updated_count += 1
        
    return updated_count

if __name__ == "__main__":
    # Test run
    asyncio.run(update_college_fees())
