import datetime
from flask import flash, request

class Ticket:
    
    
    def __init__(self):
        self.ticket_content = request.form['ticket_content']
        self.status = "Not Responded"
        self.ticket_category = request.form['ticket_category']
        self.timestamp = datetime.datetime.now()

    def save_to_db(self, collection):
        collection.insert_one({
            'ticket_content': self.ticket_content,
            'status': self.status,
            'category':self.ticket_category,
            'timestamp': self.timestamp
        })
        flash('Your Request submitted successfully', 'success')
    
    # def Edit():
    #     pass