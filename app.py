import streamlit as st 
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('logistic_reg_model.pkl','rb'))
scaler = pickle.load(open('normaliser.pkl','rb'))

stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    text = [word for word in text if word.isalnum() and word not in stopwords.words('english') ]
    text = [stemmer.stem(word) for word in text]
    return ' '.join(text)

st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter the message")


if st.button("Predict"):
    # preproceess
    clean_text = preprocess_text(input_sms)

    # vectorize
    vector_input = tfidf.transform([clean_text]).toarray()

    # scale 
    scaled_vector_input = scaler.transform(vector_input)

    # predict
    result = model.predict(scaled_vector_input)

    # display

    if result ==1:
        st.header("Spam")
    else:
        st.header("Not Spam")
    