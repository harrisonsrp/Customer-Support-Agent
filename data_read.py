import pandas as pd
from pymongo import MongoClient

def read_data_from_mongodb():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    
    # Assuming your database name is 'mydatabase' and collection name is 'mycollection'
    db = client['hotel_reviews']
    collection = db['data']
    
    
    # Query MongoDB and fetch data
    cursor = collection.find({}).limit(3)

    
    return cursor

