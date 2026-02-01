import requests
import streamlit as st

def get_response(user_input):
    api_url = "http://localhost:8000/chat/invoke"
    payload = {
        "input": {"input": user_input}
    }
    response = requests.post(api_url, json=payload)
    return response.json()["output"]["content"]

def main():
    st.title("Programming Language Learning Planner")

    with st.form('my_form'):
        user_input = st.text_area('Enter text:')
        submitted = st.form_submit_button('Submit')
        if submitted:
            response = get_response(user_input)
            st.subheader("Learning Plan:")
            st.write(response)


if __name__ == "__main__":
    main()