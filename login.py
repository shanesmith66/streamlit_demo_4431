import streamlit as st

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Submit"):
        if username == "admin" and password == "password":
            st.success("Login Successful")
            st.stop()
        else:
            st.error("Wrong credentials")

if __name__ == '__main__':
    login()