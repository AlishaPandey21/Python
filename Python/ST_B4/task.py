from numpy import random 
import streamlit as st

st.sidebar.title("Student Info")
name=st.text_input("Enter Your Name")
bt=st.button("Generate Random Number")
if bt==True:
    num=random.randint(1,101)
    if num>50:
        # st.image("tiger.jpeg")
        st.image("https://picsum.photos/600/300")
    else:
        st.video("https://youtu.be/y65YdfJMxbU?si=Bvoi2zto0LfUGtYX")
        
