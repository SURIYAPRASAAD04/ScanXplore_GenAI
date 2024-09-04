import google.generativeai as genai
import os


os.environ["API_KEY"] = "AIzaSyBsr3pZ08vj-Mjg-6aoDG6lS59oqtsTbts"


genai.configure(api_key=os.environ["API_KEY"])


def fetch_product_details(product_name):
    prompt = f"""
    Please provide short information about the product '{product_name}' including:
    short Product Description and current price in dollar (dont put any star, headings)
     instruction make it in 1 lines
    """

    model = genai.GenerativeModel('gemini-1.5-flash')

  
    response = model.generate_content(prompt)

    return response.text

def fetch_product_rating(product_name):
    prompt = f"""
    Please provide information about the product '{product_name}' 
    overall Product star rating of that brand in numbers like (4.5,3.2...ect) (dont put any star, headings,points)
    """


    model = genai.GenerativeModel('gemini-1.5-flash')

  
    response = model.generate_content(prompt)

    return response.text

def fetch_product_review(product_name):
    prompt = f"""
<<<<<<< HEAD
    Please provide overall(positive and negative) very short review of the product '{product_name}' 
=======
    Please provide short information about the product '{product_name}' 
    product review of 3 customer (dont put any star, headings,points)
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f
    instruction make it in 2 lines
    """

 
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)

    return response.text

def fetch_product_trends(product_name):
    prompt = f"""
    Please provide short information about the product '{product_name}' 
    products social trends (dont put any stars, headings,points,hash tags) just make is as a short paragraph
    instruction make it in 1 lines
    """


    model = genai.GenerativeModel('gemini-1.5-flash')

 
    response = model.generate_content(prompt)

    return response.text

def fetch_product_similar(product_name):
    prompt = f"""
    Please provide information about some 5 similar products (list by comma seperating) of the product '{product_name}' 
    (dont put any star, headings,points)
    """


    model = genai.GenerativeModel('gemini-1.5-flash')


    response = model.generate_content(prompt)

    return response.text