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

if __name__ == '__main__':
    chat()