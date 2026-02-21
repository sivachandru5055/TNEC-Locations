
import asyncio
from database import db
from models import College
from bson import ObjectId

async def test_validation():
    college_data = await db['colleges'].find_one()
    if not college_data:
        print("No colleges in DB")
        return
    
    college_id = str(college_data['_id'])
    print(f"Testing validation for ID: {college_id}")
    
    college_data['_id'] = str(college_data['_id'])
    try:
        college_obj = College(**college_data)
        print("Validation Successful!")
        print(college_obj.model_dump())
    except Exception as e:
        print(f"Validation Failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_validation())
