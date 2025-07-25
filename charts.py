import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for rendering charts
import matplotlib.pyplot as plt
import uuid 
import os 

def cleanup_charts(output_dir='static'):
    """ Cleans up old chart images in the specified output directory."""
    for file in os.listdir(output_dir):
        if file.endswith('.png'):
            try:
                os.remove(os.path.join(output_dir, file))
            except Exception as e:
                print(f"Error removing file {file}: {e}")

def generate_pie_chart(emotions, output_dir='static'):
    """ Generates a pie chart from the given emotions data."""
    cleanup_charts(output_dir)  # Clean up old charts before generating a new one

    filtered_emotions = {k: v for k, v in emotions.items() if v > 0}  # Filter out emotions with zero values
    chart_id= str(uuid.uuid4()) # Generate a unique ID for the chart
    chart_path= os.path.join(output_dir, f'{chart_id}.png') # Create the full path for the chart image
    
    plt.figure(figsize= (6,6)) # Set the figure size
    plt.pie(filtered_emotions.values(), labels=filtered_emotions.keys(), autopct= '%1.1f%%', startangle= 140) # Create a pie chart with the emotions data
    plt.title= 'Emotions Distribution'
    plt.axis= "equal"  # Equal aspect ratio ensures that pie chart is a circle
    plt.tight_layout()  # Adjust layout to prevent clipping of pie chart
    plt.savefig(chart_path)  # Save the chart to the specified path
    plt.close()  # Close the plot to free up memory
    
    return chart_path  # Return the path to the saved chart image


