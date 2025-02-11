import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('stopwords')

#load a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model = "distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please contact Doctor for accurate advice. "
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the Doctor? "
    elif "medication" in user_input:
        return "It's important to take prescribed medication regularly. If you have concerns, consult your doctor. "
    else:
        response = chatbot(user_input, max_length = 300, num_return_sequences = 1)
        return response[0]['generated_text']


#Streamlit web app interface
def main():
    st.title("Healthcare Assistant Chatbot ")
    user_input = st.text_input("How can I assist you today? ")

    if st.button("Submit"):
        if user_input:
            st.write("User : ", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant : ", response)
        else:
            st.write("Please enter a message to get a response. ")
if __name__=="__main__":
    main()