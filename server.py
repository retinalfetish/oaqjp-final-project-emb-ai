"""
Flask server for an emotion detector API.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    """
    Accept a text string and return an AI analyzed response.
    """
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    keys = list(result.keys())
    values = list(result.values())

    response = (
        f"For the given statement, the system response is "
        f"'{keys[0]}': {values[0]}, "
        f"'{keys[1]}': {values[1]}, "
        f"'{keys[2]}': {values[2]}, "
        f"'{keys[3]}': {values[3]}, "
        f"and '{keys[4]}': {values[4]}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    # for k, v in result.items():
    #     response = response + f"'{k}': {v}, "

    return response

@app.route("/")
def index():
    """
    Return the index page template.
    """
    return render_template("index.html")
