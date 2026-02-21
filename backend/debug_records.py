import asyncio
from database import db
from models import College
from pydantic import ValidationError

async def check_records():
    print("Checking college records...")
    cursor = db["colleges"].find()
    count = 0
    errors = 0
    async for college in cursor:
        college["_id"] = str(college["_id"])
        try:
            College(**college)
            count += 1
        except ValidationError as e:
            errors += 1
            print(f"Error in record {college.get('code')} - {college.get('name')}:")
            print(e)
    
    print(f"\nSummary: {count} valid records, {errors} errors found.")

if __name__ == "__main__":
    asyncio.run(check_records())
