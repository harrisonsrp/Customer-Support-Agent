from flask import Flask, render_template, render_template, request, redirect, jsonify
from datetime import datetime
from data_crud import read_mongodb
# Create Flask app instance
app = Flask(__name__)



####### Start Routes #######

# Recent Reviews Route
@app.route('/')
def index():
    # cursor  = ...
    return render_template('index.html')



# Send Reviews Route
@app.route('/sendReview')
def sendReview():
    #red data from mongodb
    return render_template('reviews/index.html')


####### End Routes #######


# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
