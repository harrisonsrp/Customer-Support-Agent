from flask import Flask, render_template, render_template, request, redirect, jsonify,flash
from datetime import datetime
from database_conn import collection, cursor
# Create Flask app instance
app = Flask(__name__)
app.secret_key = '##Secret##' #for flash


####### Start Routes #######

# Recent Reviews Route
@app.route('/')
def index():
    cursor  = collection.find({})
    return render_template('index.html', data = cursor)



# Send Reviews Page Route
@app.route('/sendReview')
def sendReview():
    #red data from mongodb
    return render_template('reviews/index.html')
# Write review to database
@app.route('/submitReview', methods=['POST'])
def submit_review():
    if request.method == 'POST':
        review_content = request.form['review_content']
        timestamp = datetime.now()  # Get current timestamp
        # Insert the review into MongoDB
        collection.insert_one({'review_content': review_content, 'timestamp': timestamp})
        flash('Review submitted successfully', 'success')
        return redirect('/sendReview')

####### End Routes #######


# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
