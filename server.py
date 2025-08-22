"""
server.py

Flask server for Emotion Detection application.
Provides routes for homepage and emotion analysis API.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def detect_emotion():
    """
    Receives text from query parameters, analyzes emotion using the
    emotion_detector function, and returns a readable response.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is {response}"

@app.route('/')
def index_home():
    """
    Renders the main index page of the application.
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
