
from models import College
from pydantic import ConfigDict
import json

def test_serialization():
    data = {
        "_id": "507f1f77bcf86cd799439011",
        "name": "Test College",
        "location": "Chennai",
        "type": "Private",
        "affiliated_to": "Anna University",
        "fees_btech": 100000,
        "fees_mtech": 50000,
        "avg_package": 500000,
        "latitude": 13.0,
        "longitude": 80.0
    }
    
    college = College(**data)
    print("Normal Dump:", college.model_dump())
    print("Alias Dump:", college.model_dump(by_alias=True))
    
    # Simulate FastAPI serialization
    from fastapi.encoders import jsonable_encoder
    print("FastAPI Encoded (No Alias):", jsonable_encoder(college))
    print("FastAPI Encoded (By Alias):", jsonable_encoder(college, by_alias=True))

if __name__ == "__main__":
    test_serialization()
