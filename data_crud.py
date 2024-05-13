#This file is for the connection with MongoDB database
import pandas as pd
from pymongo import MongoClient

def read_mongodb():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    
    # Connect to database to recent reviews and show it on admin side
    db = client['hotel_reviews']
    collection = db['Review']
    
    
    # Query MongoDB and fetch data
    cursor = collection.find({}).limit(3)

    
    return cursor

