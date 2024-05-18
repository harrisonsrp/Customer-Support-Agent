#This file is for the connection with MongoDB database
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
    
# Connect to database to recent reviews and show it on admin side
db = client['Customer_support']

#tickets collection
collection_tickets = db['tickets']

#raw data collection
collection_raw_data = db['raw_data']

#FAQ Collection
collection_faq = db['faq']

#FAQ category Collection
collection_faq_cat = db['faq_category']
# #clean_data
# collection_clean_data = db['clean_data']

# # Embedded data for sentiment analysis
# collection_embedded_data_sa = db['embedded_data_sa']


