import streamlit as st
import pandas as pd
import time
st.sidebar.title("STUDENT INFO")
sub=st.sidebar.selectbox("Select Subject",["fsd-1","python-1","ps","DE"])
s=st.sidebar.radio("select type",["group","Individual"])
data={"name":["dhruv","rahul","sonam","anita"],"age":[20,21,22,20]}
df=pd.DataFrame(data)
st.header("dataframe")
st.dataframe(df)
st.header("table")
st.table(df)
st.json(data)
h=st.file_uploader("Upload File",type={"png","jpeg","jfif"})

if st.button("upload"):
 st.image(h)

if st.button("submit"):
    x=st.progress(0)
    with st.spinner("loading......"):
        for i in range(100):
           
            time.sleep(0.1)
            x.progress(i+1)
    st.success("Submitted Successfully")


    