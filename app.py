from flask import Flask, render_template, render_template, request, redirect, jsonify
from Database import collection_tickets, collection_faq,collection_faq_cat


#Objects
from Ticket import *
from FAQ import *
# Create Flask app instance
app = Flask(__name__)
app.secret_key = '##Secret##' #for flash


####### DataBase Collections ####
ticket_coll = collection_tickets
faq_coll = collection_faq
faq_cat_coll = collection_faq_cat
####### Start Routes #######

# Recent Reviews Route
@app.route('/')
def index():
    data_ticekt = ticket_coll.find({})
    return render_template('index.html', data=data_ticekt)


# New ticket Page Route
@app.route('/sendTicket')
def sendTicket():
    category = faq_cat_coll.find({})
    return render_template('tickets/create.html', category = category)


# Write ticket to database
@app.route('/submitTickets', methods=['POST'])
def submit_ticket():
    if request.method == 'POST':
        # Pass input data in Ticket class
        get_ticket_data = Ticket()
        # Save data to DB
        get_ticket_data.save_to_db(ticket_coll)
        # Return to main page
        return redirect('/sendTicket')

# FAQ Route
@app.route('/faq')
def faq():
    data_faq  = faq_coll.find({})
    return render_template('faq/FAQ.html', data = data_faq)

# show ticket Page Route
@app.route('/faq_create')
def faq_create():
    category = faq_cat_coll.find({})
    return render_template('faq/create.html', category = category)


# Write faq to database
@app.route('/submitFAQ', methods=['POST'])
def submitFAQ():
    if request.method == 'POST':
        # Get FAQ data
        get_faq_data = FAQ()
        # Save to DB
        get_faq_data.save_to_db(faq_coll)
        return redirect('/faq')



####### End Routes #######


# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
