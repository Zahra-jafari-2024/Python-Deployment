import streamlit as st
import pandas as pd
st.title("BMI CALCULATOR")
st.write("This calculator provides body mass index (BMI) and the corresponding BMI weight status category ")

weight=st.number_input("Enter your Waight (Kg)")
height=st.number_input("Enter your height (cm)")
st.write("")
BMI_btn=st.button("click me")
col1,col2=st.columns(2)
if BMI_btn:
    height1=height/100
    bmi=(weight/(height1**2))
    if bmi<=18.5:
        st.info(f"BMI={bmi:.2f}... You are Underweight")
    if 18.5<bmi<=24.9:
        st.success(f"BMI={bmi:.2f}...You are Normal")
    if 25<bmi<=29.9 :
        st.warning(f"BMI={bmi:.2f}...You are overweight")    
    if  30<bmi<=34.9 :
        st.error(f"BMI={bmi:.2f}...You are Obese")   
    if  bmi>35 :
        st.error(f"BMI={bmi:.2f}...You are Extermly Obese")         
    with col1:
       st.dataframe(pd.DataFrame({
          'BMI': ['less than 18.5' , 'Between 18.5 and 24.9' ,'Between 25 and 29.9' , 'Between 30 and 34.9','More than 35'],
          'Status': ['Underweight', 'Normal', 'overweight', 'Obese','Extermly Obese']
        }))
    with col2:
       st.image("./IMAGE/BMI1.jpg") 
