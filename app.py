import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCDoCNQpIBEbnH5tfy_FjL6DvNaJpd75NI")

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("📘 ExamPrep Copilot")

question = st.text_input("Enter Exam Question")
marks = st.selectbox("Select Marks", ["5", "10"])
student_answer = st.text_area("Enter Your Answer (Optional)")

if st.button("Generate Examiner Answer"):
    prompt = f"""
    You are a university examiner.
    Generate a {marks}-mark answer.
    Use headings and highlight keywords.
    Question: {question}
    """
    response = model.generate_content(prompt)
    st.write(response.text)

if st.button("Evaluate My Answer"):
    prompt = f"""
    You are a university examiner.
    Evaluate the student's answer out of {marks}.
    Give marks and improvement suggestions.
    Question: {question}
    Student Answer: {student_answer}
    """
    response = model.generate_content(prompt)
    st.write(response.text)
