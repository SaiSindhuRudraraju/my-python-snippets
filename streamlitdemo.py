import streamlit as st
import pandas as pd

title = "Streamlit Demo"
st.title(title)
st.write("This is a simple Streamlit application.")
button_clicked = st.button("Click Me!!")

st.write(button_clicked)

st.text_input("Enter some text...:")

df = pd.DataFrame([[1,2],[3,4]], columns=["A", "B"])
st.write(df)

file = st.file_uploader("Uploas a file:")
if file is not None:
    tempdf = pd.read_csv(file)
    st.write(tempdf)

if button_clicked:
    st.write("Button Clicked!")
    title = "Hello"