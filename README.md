# ATS Tracking System

A Streamlit-based web app that uses Google Gemini LLM to analyze and improve resumes against job descriptions, simulating an Applicant Tracking System (ATS) and HR review.

## Features
- Upload your resume (PDF)
- Paste a job description
- Get a professional evaluation and ATS match percentage
- Suggestions to improve your resume

## How to Run
1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Set up your Google API key and .env file
4. Run: `streamlit run streamlit_app.py`

## Technologies
- Streamlit
- Google Gemini LLM
- PDF processing (PyPDF2, pdf2image)
