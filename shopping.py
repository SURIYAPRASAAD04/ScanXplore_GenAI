import google.generativeai as genai
import os


os.environ["GOOGLE_API_KEY"] = "AIzaSyBsr3pZ08vj-Mjg-6aoDG6lS59oqtsTbts"


genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def generate_walmart_links(product_name):
    """Construct the Walmart search URL for the specified product."""
    base_url = "https://www.walmart.com/search/?query="
    product_query = product_name.replace(' ', '+')  
    search_url = f"{base_url}{product_query}"
    return search_url

def main(product_name):
    
    walmart_link = generate_walmart_links(product_name)

    return walmart_link

