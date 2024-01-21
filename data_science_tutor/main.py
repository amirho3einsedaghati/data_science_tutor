import streamlit as st
from chatbot import chatbot



# Streamlit application
def combined_model():  
    st.title("Data Science Assistant")
    curr_question = st.text_area(
        'enter your prompt',
        placeholder="Talk to your Data Science Tutor: ",
        label_visibility="hidden"
    )
    if st.button("Generate Answer"):
        try:
            chatbot(curr_question)
        except:
            st.warning(body="Refresh the page or Try it again later.", icon="🤖")

combined_model()

