import google.generativeai as genai
import os


os.environ["API_KEY"] = "AIzaSyCK8Se8EfYf-qf6zTYCXU0WsaiUunhwOew"


def fetch_review(product_name):
    prompt = f"""
    customer review of the product '{product_name}' 
    instruction to make it as one customer review in 30 words just make is as a short paragraph
    instruction make it in 1 lines and dont need any heading for this
    """

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)

    return response.text

