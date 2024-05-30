import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.title("image Blure App")
number=int(st.slider("please enter a Percent of blur",min_value=1,max_value=100,value=1,step=2))
uploadimage=st.file_uploader("Select your Image ...",type=["jpg","jpe","png"])
btn=st.button("Image Prossesing")
if btn:
    col1 , col2 = st.columns(2)
    with col1:
        st.image(uploadimage,"Input Image")
        image=Image.open(uploadimage)
        image=np.array(image)
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        resultimage=cv2.blur(image,(number,number))
        result_image=cv2.cvtColor(resultimage,cv2.COLOR_BGR2RGB)
        result_image=Image.fromarray(result_image)
    with col2:    
        st.image(result_image,"Result Image")
