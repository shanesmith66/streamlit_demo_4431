import streamlit as st

def chat():
    st.title("Chat Page")
    messages = []
    message = st.text_input("Enter a message")
    if st.button("Send"):
        messages.append(message)
    st.write("Messages:")
    for msg in messages:
        st.write("- " + msg)


def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Submit"):
        if username == "admin" and password == "password":
            st.success("Login Successful")
            with st.spinner("Loading chat page..."):
                chat()
            st.stop()
        else:
            st.error("Wrong credentials")

login()
