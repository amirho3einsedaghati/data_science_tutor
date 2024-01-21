from openai import OpenAI
import streamlit as st
from moderator import moderator



gpt_model = 'gpt-3.5-turbo'
client = OpenAI(
    # Read the OpenAI API key from the environment variable
    # api_key = os.environ.get('OPENAI_API_KEY')
    api_key= "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"
)

messages = [
    {
        'role' : "system",
        'content' : "You are a data science tutor who provides short, simple, clear answers.\
                     You can't provide information on a wide range of topics beyond data science and programming."
    },
    {
        'role' : 'user',
        'content' : 'Tell me about yourself.'
    },
    {
        'role' : 'assistant',
        'content' : "I am a data sciece assistant. My purpose is to assist users by providing concise and\
                     accurate answers in the topics related to data such as data science, programming, mathematics,\
                     Artificial Intelligence, Machine Learning, Deep Learning, Databases, Data Engineering, and more." 
    },
    {
        'role' : 'user',
        'content' : 'Can you provide information in topics not related to data science and programming?'
    },
    {
        'role' : 'assistant',
        'content' : "No, I'm here to assist you in data related fields such data science, programming,\
                     mathematics and more." 
    }   
]


# GPT-3.5 response generation
def chatbot(prompt:str):  
    flagged = moderator(prompt)
    st.write('User: ', prompt)
    if flagged == True:
        st.warning("Assistant: The latest request violates OpenAI's content policies. Please change it.\n",  "🚨")

    else:
        user_dict = {'role' : 'user', 'content' : prompt}
        messages.append(user_dict)

        res = client.chat.completions.create(
            model=gpt_model,
            messages=messages
        )
        assistant_dict = {'role' : res.choices[0].message.role, 'content' : res.choices[0].message.content}
        messages.append(assistant_dict)
        st.write("Assistant: ", assistant_dict['content'], "\n")
    

