''' A Flask application for emotion detection using the
 Watson NLP library, deployed on localhost:5000.'''

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("__name__")

@app.route('/emotionDetector', methods=['GET'])
def detect():
    '''
    This function takes a statement from the HTML 
    page and utilizes the emotion_detector() function to perform emotion detection.
    The output is a string containing the set of emotions with their respective scores and
    the dominant emotion for the provided statement.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return ("For the given statement, the system response is "
    + ", ".join([f"'{emotion}': {score}" for emotion, score in
    response.items() if emotion not in ('dominant_emotion', 'sadness')])
    + f" and 'sadness': {response['sadness']}."
    + f"The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    '''This function runs the render_template function on the index.html.'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
