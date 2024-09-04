import google.generativeai as genai
import os

os.environ["API_KEY"] = "AIzaSyBsr3pZ08vj-Mjg-6aoDG6lS59oqtsTbts"

genai.configure(api_key=os.environ["API_KEY"])


def fetch_social_trends(product_name):
    prompt1 = f"""
    Please provide very short information about the product '{product_name}' 
    say the products social trends article referrence content (dont put any stars, headings,points,hash tags) just make is as a short paragraph
    instruction make it in 1 lines
    """

    model = genai.GenerativeModel('gemini-1.5-flash')

    response1 = model.generate_content(prompt1)



    prompt2 = f"""
    The product is '{product_name}' 
    say the products random users(in numbers) across the world (dont put any stars, headings,points,hash tags) just make is as a short paragraph
    instruction make it in 1 lines
    """

    model = genai.GenerativeModel('gemini-1.5-flash')

    response2 = model.generate_content(prompt2)



    prompt3 = f"""
    The product is '{product_name}' 
    how is famous nowdays ?(dont put any stars, headings,points,hash tags) just make is as a short paragraph
    instruction make it in 1 lines
    """

    model = genai.GenerativeModel('gemini-1.5-flash')

    response3 = model.generate_content(prompt3)



    prompt4 = f"""
    The product is '{product_name}' 
    tell about future updates for that product ?(dont put any stars, headings,points,hash tags) just make is as a short paragraph
    instruction make it in 1 lines
    """

    model = genai.GenerativeModel('gemini-1.5-flash')


    response4 = model.generate_content(prompt4)

    return response1.text, response2.text, response3.text, response4.text


