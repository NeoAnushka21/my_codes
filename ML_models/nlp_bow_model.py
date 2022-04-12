import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

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
cv = CountVectorizer(max_features=2000)
X = cv.fit_transform(corpus).toarray()
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# training the naive bayes model
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# predicting test results
y_pred = classifier.predict(X_test)
# print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))


cm = confusion_matrix(y_test, y_pred)
print(cm)
score = accuracy_score(y_test, y_pred)
print(score)

# predicting result for new text input
input_text = "i visted this restro"

# input_text = str(input("enter any text:"))

test_corpus = []
input_text = re.sub('[^a-zA-Z]', ' ', input_text)
input_text = input_text .lower()
input_text = input_text .split()

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

print(max(new_y_pred_score[0]))

