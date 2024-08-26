"""
server.py

This module sets up a Flask application that provides emotion detection
services using the Emotion Detection API. The application is accessible
via localhost:5000.

Routes:
- /emotionDetector: Processes input text for emotion detection.
- /: Renders the main index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detection")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    This function receives the text from the HTML interface and
    runs emotion detection using the emotion_detector() function.
    Returns a formatted string with the detected emotions and the dominant emotion.
    """
    text = request.args.get('textToAnalyze', '').strip()
    if not text:
        return "No text provided. Please enter some text to analyze."
    emotion_response = emotion_detector(text)
    # Extract emotions and the dominant emotion
    anger = emotion_response.get('anger', 0)
    disgust = emotion_response.get('disgust', 0)
    fear = emotion_response.get('fear', 0)
    joy = emotion_response.get('joy', 0)
    sadness = emotion_response.get('sadness', 0)
    dominant_emotion = emotion_response.get('dominant_emotion')
    # Check if dominant_emotion is None and return an error message if so
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    response_str = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return response_str

@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
