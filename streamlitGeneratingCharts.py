import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

title = "hi"
st.title(title)
st.write("This is a simple streamlit application.")

button_clicked = st.button("Click me!")
generate_chart = st.button("Generate Chart")

st.text_input("Enter some text:")
file = st.file_uploader("Upload a file:")

if button_clicked:
    if file is not None:
        df = pd.read_csv(file)
        st.write(df)
        df.set_index('sname', inplace=True)        #For taking sname as index(y axis)
        st.bar_chart(df)

if generate_chart:
    data = {
        "Fruits": ["Apples", "Bananas", "Cherries"],
        "Quantities": [10, 20, 15]
    }
    fig, ax = plt.subplots()
    ax.bar(data["Fruits"], data["Quantities"], color=["red", "yellow", "pink"])

    ax.set_title("Simple Chart")
    ax.set_xlabel("Fruits")
    ax.set_ylabel("Quantities")

    st.pyplot(fig)