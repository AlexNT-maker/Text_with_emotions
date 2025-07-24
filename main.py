# The main.py will build with flask. Will be used to run the application. Also will include the routes.
from flask import Flask, render_template, request
from charts import generate_pie_chart
import os

# This is the main Flask application file.
app = Flask(__name__)

# Define a simple route for the home page
@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/analyze', methods=[ 'POST' ])
def analyze():
    """Render the analysis page."""
    user_text = request.form.get('user_text')

    emotions = {
        "Joy": 50,
        "Anger": 20,
        "Sadness": 15,
        "Surprise": 10,
        "Fear": 5
    }

    chart_path = generate_pie_chart(emotions)
    chart_filename= os.path.basename(chart_path)  # Get the filename from the full path

    return render_template('results.html', user_text=user_text, chart_filename= chart_filename)


if __name__== '__main__':
    # Run the Flask application
    app.run(debug=True) 

