# Importing required libraries
# flask - for creating web applications
# render_template - render_template is used to generate output from a template file
# request - contains all the data that is sent from the client to the server
from flask import Flask, render_template, request

# using vader (a pretrained model for sentiment analysis)
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Creating flask app
app = Flask(__name__, template_folder='template')


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":

        # to fetch input_text from the form in html file
        input_text = request.form.get('input_text')

        # creating an object for SentimentIntensityAnalyzer
        sia = SentimentIntensityAnalyzer()

        # storing the polarity score in score variable
        score = sia.polarity_scores(input_text)

        # checking the sentiment if it is +ve ,-ve or neutral
        if score["compound"] >= 0.05:
            return render_template('home.html', message="Positive", value=score)
        elif 0.05 > score["compound"] > -0.05:
            return render_template('home.html', message="Neutral", value=score)
        else:
            return render_template('home.html', message="Negative", value=score)

    return render_template('home.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
