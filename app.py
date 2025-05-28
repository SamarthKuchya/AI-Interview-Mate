import streamlit as st
from dotenv import load_dotenv
from google import genai
import os
load_dotenv()

def get_ai_response(file_content):
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        
    prompt = f"""You are an AI assistant that helps generate interview questions based on resume content. Given a candidate's resume, return the top 15 interview questions (technical, behavioral, and situational) tailored to their skills, experience, and qualifications. Use the examples below to guide your responses.

    Example 1:
    Resume Summary:

    Role: Software Developer

    Skills: Java, Spring Boot, REST APIs, MySQL, Git

    Experience: 2 years backend development

    Projects: E-commerce API, Task Management System

    Generated Questions:

    Can you explain the architecture of the e-commerce API you developed?

    How have you used Spring Boot in your recent projects?

    Describe a time when you optimized a database query.

    How do you manage version control using Git in a team setting?
    ... (up to 15 questions)

    Example 2:
    Resume Summary:

    Role: Data Analyst

    Skills: Python, Pandas, SQL, Power BI, Data Visualization

    Experience: 1 year internship, 3 personal projects

    Certifications: Microsoft Power BI, Google Data Analytics

    Generated Questions:

    Walk me through how you used Power BI to visualize data trends.

    How do you handle missing or inconsistent data in a dataset?

    Tell me about a challenging analysis project and how you approached it.

    How proficient are you in writing complex SQL queries?
    ... (up to 15 questions)

    Now use this format for the uploaded resume:

    Resume:
    {file_content}

    Your Task:
    Generate 15 tailored interview questions (technical + behavioral) based on the resume content.

    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )
    return response.text

st.set_page_config(page_title="AI Interview Questions Generator", layout="centered")
with st.sidebar:
    st.title("Upload your resume (PDF or DOCX)")
    uploaded_file = st.file_uploader("",type=["pdf", "docx"])
    
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        st.write("File Name:", uploaded_file.name)
        file_content = uploaded_file.read()
    button=st.button("Generate Interview Questions")
        
        
if button:
    with st.spinner("Generating questions..."):
        response = get_ai_response(file_content.decode('utf-8', errors='ignore'))
        st.write(response)
        st.success("Questions generated successfully!")