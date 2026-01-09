import streamlit as st
st.title("PROJECT-1")
x=st.sidebar.title("This is sidebar")
batch=st.sidebar.selectbox("Enter Your Batch",["B1","B2","B3","B4"])
gender=st.sidebar.radio("Select Gender",["MAle","Female"])
sub=st.sidebar.selectbox("Enter Subject For Project",["FSD","Python",])
if sub=="Python":
    st.title("Welcome To Python World")
    enroll=st.text_input("Enter Your Enrollment Number")
    pro_name=st.text_input("Enter Your Project Name")
    pro_des=st.text_area("Enter Your Project Description")
    bt=st.button("Submit")
    if bt==True:
        st.write("Your Current Batch",batch)
        st.write(gender)
        st.write(sub)
else:
    st.title("Welcome To FSD-World")
    enroll1=st.text_input("Enter Your Enrollment Number")
    pro_name1=st.text_input("Enter Your Project Name")
    pro_des1=st.text_area("Enter Your Project Description")
    bt=st.button("Submit")

