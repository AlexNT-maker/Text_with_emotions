# The main.py will build with flask. Will be used to run the application. Also will include the routes.
from flask import Flask, render_template, request
from charts import generate_pie_chart
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import TextClassificationPipeline 
import os

# This is the main Flask application file.
app = Flask(__name__)

model_name = "bhadresh-savani/distilbert-base-uncased-emotion"

tokenizer = AutoTokenizer.from_pretrained(model_name) # Load the tokenizer
model = AutoModelForSequenceClassification.from_pretrained(model_name) # Load the model

analyzer = TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=True) # Create a text classification pipeline
# Define a simple route for the home page
@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/analyze', methods=[ 'POST' ])
def analyze():
    user_text = request.form.get('user_text')

    results = analyzer(user_text)  # Analyze the user text

    emotions = {}
    # Process the results to extract emotions and their scores
    for item in results[0]: 
        label = item['label'].capitalize()  # Capitalize the label for better readability
        score = item['score']
        if score > 0.001:
            emotions[label] = round(score * 100, 1)  # Convert score to percentage, round to 1 decimal place
        
        
        

    chart_path = generate_pie_chart(emotions)
    chart_filename= os.path.basename(chart_path)  # Get the filename from the full path

    return render_template('results.html', user_text=user_text, chart_filename= chart_filename)


if __name__== '__main__':
    # Run the Flask application
    app.run(debug=True) 

