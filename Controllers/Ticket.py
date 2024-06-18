from Database import db
from datetime import datetime
from flask import flash, request, redirect, url_for
from Category import Categories

## Database Connection
class Tickets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_content = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Categories', backref=db.backref('tickets', lazy=True))

    def __repr__(self):
        return f"<Ticket {self.id}>"
    
    
    @classmethod
    def create(cls, form_data): 
        new_ticket = cls(ticket_content=form_data.ticket_content,
                         category_id=form_data.category_id,
                         user_id=form_data.user_id, 
                         status=form_data.status, 
                         timestamp=form_data.timestamp
                         )
        db.session.add(new_ticket)
        db.session.commit()
        flash('Ticket submitted successfully', 'success')





    @classmethod
    def read(cls):
        return cls.query.all()

    def update(self, ticket_content=None, status=None, timestamp=None):
        if ticket_content:
            self.ticket_content = ticket_content
        if status:
            self.status = status
        if timestamp:
            self.timestamp = timestamp
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def read_form(cls):
        category_id = request.form['category_id']
        ticket_content = request.form['ticket_content']
        user_id = 1  # This should be dynamic, e.g., from the session or current user
        status = "Not Responded"
        timestamp = datetime.now()
        return cls(category_id=category_id, ticket_content=ticket_content, user_id=user_id, status=status, timestamp=timestamp)

    