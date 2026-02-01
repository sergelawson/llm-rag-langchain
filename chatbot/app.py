import warnings
import os
from dotenv import load_dotenv

# Suppress Pydantic v1 compatibility warnings BEFORE importing langchain
warnings.filterwarnings("ignore", category=UserWarning)

from langchain_openai import ChatOpenAI
import streamlit as st

def generate_response(llm, message, user_input):
    message.append(("human", user_input))
    response = llm.invoke(message)
    message.append(("assistant", response.content))
    return response.content

def main():
    load_dotenv()

    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["LANGSMITH_TRACING"]="true"
    os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"
    os.environ["LANGSMITH_API_KEY"]= os.getenv("LANGSMITH_API_KEY")
    os.environ["LANGSMITH_PROJECT"]="programming-language-learning-planner"


    llm = ChatOpenAI(model_name="gpt-4.1-nano", temperature=1)

    message = [("system", "You are a helpful assistant that will help me plan my learning of a programming language in 4 steps.")]
    
    st.title("Programming Language Learning Planner")

    with st.form('my_form'):
        user_input = st.text_area('Enter text:')
        submitted = st.form_submit_button('Submit')
        if submitted:
            response = generate_response(llm, message, user_input)
            st.subheader("Learning Plan:")
            st.write(response)








if __name__ == "__main__":
    main()
