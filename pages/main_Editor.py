import streamlit as st

st.title("Void Entertainment Login")
st.text_area(
    "Main Editor" 
    ,value = "(Place content in the container to post it to website)"
    ,height = 400
)


st.text_input("Post Title")
st.button("Publish Post")