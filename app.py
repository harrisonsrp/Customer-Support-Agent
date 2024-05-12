from flask import Flask, render_template, render_template, request, redirect, jsonify
from datetime import datetime
from data_read import read_data_from_mongodb
# Create Flask app instance
app = Flask(__name__)



####### Start Routes #######

# Data Analyst Route
@app.route('/')
def index():
    cursor  = read_data_from_mongodb()
    return render_template('index.html', data=cursor)


####### End Routes #######


# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
