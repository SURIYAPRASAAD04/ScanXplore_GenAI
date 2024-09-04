import google.generativeai as genai
import os


os.environ["API_KEY"] = "AIzaSyBsr3pZ08vj-Mjg-6aoDG6lS59oqtsTbts"


genai.configure(api_key=os.environ["API_KEY"])

def fetch_review1(product_name):
    prompt = f"""
    customer review of the product '{product_name}' 
    instruction to make it as one customer negative review in 30 words just make is as a short paragraph
    instruction make it in 1 lines and dont need any heading for this
    """

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)

    return response.text

