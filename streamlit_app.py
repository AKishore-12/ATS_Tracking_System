from backend import get_gemini_response, input_pdf_setup, input_prompt1, input_prompt2
import streamlit as st

st.set_page_config("ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=['pdf'])

if uploaded_file:
    st.write("PDF Uploaded Successfully")
    pdf_content = input_pdf_setup(uploaded_file)

submit1 = st.button("Tell me About the Resume")
submit2 = st.button("How Can I Imporvise my resume")

if submit1:
    if uploaded_file:
        response = get_gemini_response(input_text=input_text, pdf_content=pdf_content, prompt=input_prompt1)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the PDF")

elif submit2:
    if uploaded_file:
        response = get_gemini_response(input_text=input_text, pdf_content=pdf_content, prompt=input_prompt2)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the PDF") 