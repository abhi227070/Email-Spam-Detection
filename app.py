import streamlit as st
import pickle
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
import nltk

nltk.download("punkt")

tfidf= pickle.load(open("tfidf.pkl","rb"))
model= pickle.load(open("model.pkl","rb"))

st.title("Email/SMS Spam Detection")
text = st.text_area("Enter the Email text Here:")

ps = PorterStemmer()

def transform(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words("english") and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))
  return " ".join(y)

if st.button("Predict"):
    text = transform(text)
    text = tfidf.transform([text])
    
    prediction = model.predict(text)
    
    if prediction[0] == 1:
        st.success("Spam")
        
    else:
        st.success("Not spam")
    