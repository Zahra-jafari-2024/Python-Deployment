import streamlit as st
import pandas as pd

st.title("Data Science app")
st.sidebar.title("About")
st.sidebar.write("Injury statistics – work-related claims: 2018 – CSV")

uploadfile=st.file_uploader("upload csv file")

if uploadfile:
    df = pd.read_csv(uploadfile,encoding="ISO-8859-1")
    st.write(df)
    df=df.groupby(["Year"], as_index=False)["Value"].sum()
    col1,col2=st.columns(2)
    st.write(df)
    st.line_chart(df, x="Year", y="Value")