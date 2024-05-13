#This file is for the connection with MongoDB database
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
    
# Connect to database to recent reviews and show it on admin side
db = client['hotel_reviews']
collection = db['Reviews']


# Query MongoDB and fetch data
cursor = collection.find({}).limit(3)

    


