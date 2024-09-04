import google.generativeai as genai
import os


os.environ["API_KEY"] = "AIzaSyBsr3pZ08vj-Mjg-6aoDG6lS59oqtsTbts"


genai.configure(api_key=os.environ["API_KEY"])


def fetch_details(product_name):
    prompt = f"""
Provide detailed information about the product '{product_name}' including:
1. A detailed product description, listed in numbered points.
2. clearly stated in a separate numbered point.

Please ensure each point is listed on a new line, using only numbered points (e.g., 1, 2, 3). Do not use any special characters such as stars (*) or hashtags (#) before or after any words in the sentences.
"""


    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)

    return response.text

def fetch_rating(product_name):
    prompt = f"""
    Please provide information about the product '{product_name}' 
    overall Product star rating  (dont put any star, headings,points)
    """

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)

    return response.text

<<<<<<< HEAD
=======
def fetch_review(product_name):
    prompt = f"""
    Please provide detail information about the product '{product_name}' 
    in that product review of some 3 customer 
    instruction make it as customer 1: review till 50 customer review
    """

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)

    return response.text
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f

def fetch_trends(product_name):
    prompt = f"""
    Please provide detailed information about the product '{product_name}' in
    products todays social trends in point by point (dont put any stars, headings,points,hash tags) just make is as a big paragraph
    """

    model = genai.GenerativeModel('gemini-1.5-flash')


    response = model.generate_content(prompt)

    return response.text

def fetch_similar(product_name):
    prompt = f"""
<<<<<<< HEAD
    Please provide information about some 5 similar products (list by comma seperating) of the product '{product_name}' 
    (dont put any star, headings,points) """
=======
    Please provide detailed information about some 5 similar products (list by comma seperating) of the product '{product_name}' 
    (dont put any star, headings,points)
    instruction 1. similar product name : in next line make detailed infornmation of that product , make line this for maximum 10 similar products 
    """
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)

    return response.text