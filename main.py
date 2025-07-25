# The main.py will build with flask. Will be used to run the application. Also will include the routes.
from flask import Flask, render_template, request
from charts import generate_pie_chart
from transformers import pipeline # Importing the pipeline for emotion analysis
import os

# This is the main Flask application file.
app = Flask(__name__)

analyzer = pipeline("sentiment-analysis", device=-1)  # Load the sentiment analysis pipeline
# Define a simple route for the home page
@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/analyze', methods=[ 'POST' ])
def analyze():
    """Render the analysis page."""
    user_text = request.form.get('user_text')

    emotions = {}
    suggestion = None
    label = None
    score = None

    if len(user_text.strip()) <6:
        emotions = {"Neutral": 100}  # Default emotion if text is too short
        suggestion = "Please enter more text for emotion analysis."
    
    else:
        result = analyzer(user_text)[0]  # Analyze the user text
        label = result['label']  # Get the label from the analysis result
        score = result['score']  # Get the score from the analysis result

    

    
    
    if label == 'POSITIVE':
        emotions = {"Joy": int(score * 100), "Surprise": int((1-score) * 50), "Neutral": int((1-score) * 50)}  # Positive emotions
    elif label == 'NEGATIVE':
        emotions = {"Anger": int(score * 100), "Fear": int((1-score) * 50), "Sadness": int((1-score) * 50)}  # Negative emotions

    suggestion= None
        
        

    chart_path = generate_pie_chart(emotions)
    chart_filename= os.path.basename(chart_path)  # Get the filename from the full path

    return render_template('results.html', user_text=user_text, chart_filename= chart_filename, suggestion=suggestion)


if __name__== '__main__':
    # Run the Flask application
    app.run(debug=True) 

