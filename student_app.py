import streamlit as st
from Student import Student

st.title("🎓 STUDENT MANAGEMENT SYSTEM")

name=st.text_input("enter student name")
age=st.number_input("enter age")
student_id=st.number_input("enter student ID")
marks=st.slider("enter marks",0,100,50)

if st.button("create student"):
    student = Student(name,age,student_id,marks)
    st.success("student created successfully!")
    st.subheader("student details")
    st.write(student.details())
    
