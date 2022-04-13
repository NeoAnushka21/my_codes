from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
import numpy as np
import re
import nltk

df = pd.read_csv('/home/neosoft/Downloads/Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
# print(df)

corpus = []
for i in range(1000):
    review = re.sub('[^a-zA-Z]', ' ', df['Review'][i])
    review = review.lower()
    review = review.split()

    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]

    # lm = WordNetLemmatizer()
    # review = [lm.lemmatize(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)

# print(corpus)
# creating bag of words model
count_vec = CountVectorizer(max_features=1500)
X = count_vec.fit_transform(corpus).toarray()
y = df.iloc[:, -1].values

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# Training the svc model
svc_classifier = SVC(kernel = 'linear', random_state = 0)
svc_classifier.fit(X_train, y_train)

# predicting test results
y_pred = classifier.predict(X_test)
# print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))


cm = confusion_matrix(y_test, y_pred)
print(cm)
score = accuracy_score(y_test, y_pred)
print(score)


# Creating flask app
app = Flask(__name__, template_folder='template')


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":

        # to fetch input_text from the form in html file
        input_text = request.form.get('input_text')
        test_corpus = []
        input_text = re.sub('[^a-zA-Z]', ' ', input_text)
        input_text = input_text.lower()
        input_text = input_text.split()

        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')

        # lm = WordNetLemmatizer()
        # input_text = [lm.lemmatize(word) for word in input_text if not word in set(all_stopwords)]

        input_text = [ps.stem(word) for word in input_text if not word in set(all_stopwords)]
        input_text = ' '.join(input_text)
        test_corpus.append(input_text)
        new_X_test = cv.transform(test_corpus).toarray()
        new_y_pred = classifier.predict(new_X_test)
        print(new_y_pred)
        new_y_pred_score = classifier.predict_proba(new_X_test)
        print(new_y_pred_score)
        scr = max(new_y_pred_score[0])

        # checking the sentiment if it is +ve or -ve
        if new_y_pred == 1:
            return render_template('home.html', message="Positive", value=scr)
        elif new_y_pred == 0:
            return render_template('home.html', message="Negative", value=scr)

    return render_template('home.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
