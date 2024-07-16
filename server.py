from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__) 

@app.route("/")
def home():
    return render_template("index.html")

@app.get("/emotionDetector")
def sentiment_analysis():
    textToAnalyze = request.args.get("textToAnalyze")
    result = emotion_detector(textToAnalyze)
    return result

if __name__ == "__main__":
    app.run(debug=True)