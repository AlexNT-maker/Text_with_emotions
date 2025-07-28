def generate_insight(emotions):
    """
    Generates a short natural language insight based on the emotions detected.
    The logic uses the dominant emotion to create a simple insight.
    """
    if not emotions:
        return "No emotions detected on the text."
    
    sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
    
    top_emotion, top_score = sorted_emotions[0]

    if top_score > 70:
        return f"The text predominantly expresses {top_emotion.lower()}."
    
    elif top_score > 40:
        return f"The text shows a significant presence of {top_emotion.lower()}."
    
    else:
        return "Your text contains a mix of emotions, with no dominant feeling detected."