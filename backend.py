from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
import io
import base64
import pdf2image

load_dotenv()

client = genai.Client()

def get_gemini_response(input_text, pdf_content, prompt):
    respone = client.models.generate_content(
        model='gemini-2.5-flash',
        config=types.GenerateContentConfig(
            system_instruction=prompt
        ),
        contents=[
            types.Part.from_bytes(
                data=pdf_content,
                mime_type="image/jpeg",
            ),
            input_text
        ]
    )
    return respone.text

def input_pdf_setup(uploaded_file):
    if uploaded_file:
        ## Convert the pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr

input_prompt1 = """
 You are an experienced Technical HR Manager with technical skills in Data science or Full stack or Data Engineering or Data Analyst or Artificial Intelligence or machine learning or deeplearning or MLOps,
your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of  Data science or Full stack or Data Engineering or Data Analyst or Artificial Intelligence or machine learning or deeplearning or MLOps and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
""" 