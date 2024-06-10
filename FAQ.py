from flask import flash, request
import datetime

class FAQ:
    
    def __init__(self):
        self.faq_question = request.form['faq_question']
        self.faq_answer = request.form['faq_answer']
        self.faq_category = request.form['faq_category']
        
    def save_to_db(self, collection):
        collection.insert_one({
            'category': self.faq_category,
            'question': self.faq_question,
            'answer': self.faq_answer
        })
        flash('FAQ submitted successfully', 'success')
    