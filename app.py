from flask import Flask, render_template, render_template, request, redirect, jsonify,flash
from datetime import datetime
from database_conn import collection_tickets, collection_faq,collection_faq_cat
# Create Flask app instance
app = Flask(__name__)
app.secret_key = '##Secret##' #for flash


####### Start Routes #######

# Recent Reviews Route
@app.route('/')
def index():
    cursor  = collection_tickets.find({})
    return render_template('index.html', data = cursor)

# New ticket Page Route
@app.route('/sendTicket')
def sendTicket():
    #red data from mongodb
    return render_template('tickets/index.html')


# Write ticket to database
@app.route('/submitTickets', methods=['POST'])
def submit_ticket():
    if request.method == 'POST':
        ticket_content = request.form['ticket_content']
        timestamp = datetime.now()  # Get current timestamp
        # Insert the review into MongoDB
        collection_tickets.insert_one({'ticket_content': ticket_content, 'timestamp': timestamp})
        flash('Your Request submitted successfully', 'success')
        return redirect('/sendTicket')



# FAQ Route
@app.route('/faq')
def faq():
    cursor  = collection_faq.find({})
    return render_template('faq/FAQ.html', data = cursor)

# New ticket Page Route
@app.route('/faq_create')
def faq_create():
    category = collection_faq_cat.find({})
    #red data from mongodb
    return render_template('faq/create.html', category = category)

# Write faq to database
@app.route('/submitFAQ', methods=['POST'])
def submitFAQ():
    if request.method == 'POST':
        faq_question = request.form['faq_question']
        faq_answer = request.form['faq_answer']
        faq_category = request.form['faq_category']
        timestamp = datetime.now()  # Get current timestamp
        # Insert the review into MongoDB
        collection_faq.insert_one({'question': faq_question, 'answer' : faq_answer, 'category' : faq_category, 'timestamp': timestamp})
        flash('Your FAQ submitted successfully', 'success')
        return redirect('/faq')



####### End Routes #######


# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
