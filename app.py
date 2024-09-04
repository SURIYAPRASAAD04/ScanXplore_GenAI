<<<<<<< HEAD
from flask import Flask, render_template, Response,jsonify,request,session,redirect,url_for,send_from_directory
=======
from flask import Flask, render_template, Response,jsonify,request,session,url_for,send_from_directory
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f
import cohere
from  roboflow import Roboflow
import cv2
from flask import Response, jsonify
import threading
<<<<<<< HEAD
import requests
import feedparser
from bs4 import BeautifulSoup
from social import fetch_social_trends 
from shopping import main
from ai import fetch_product_details, fetch_product_rating, fetch_product_review, fetch_product_trends, fetch_product_similar
from ai_detail import fetch_details,fetch_similar
from negative import fetch_review1
from review import fetch_review
from youtube import fetch_youtube_videos
from social import fetch_social_trends
from shopping import main
from ai import fetch_product_details, fetch_product_rating, fetch_product_review, fetch_product_trends, fetch_product_similar
from ai_detail import fetch_details, fetch_review,  fetch_similar
app = Flask(__name__)
app.secret_key = 'ScanXplore@1234'

rf = Roboflow(api_key="taUdRpwoBX8SK33QsLq1")  
project = rf.workspace().project("obj-k7ktz")  
model = project.version("1").model 

cohere_api_key = 'z9VGdW9O79SZb9Bqtu8LRjfncAtkMs4T01zSx3Jh'  
co = cohere.Client(cohere_api_key)

@app.route('/') 
def index():
    return render_template('index.html')

def remove_symbols(sentence):
    sentence = sentence.replace('*', '')
    sentence = sentence.replace('#', '')
    return sentence

@app.route('/frame')
def serve_frame():
    """Serve the frame image."""
    return send_from_directory(directory='.', path='frame.jpg')

@app.route('/about')
def about():
    product_name=session.get('productname')
    product_in = fetch_details(product_name)
    product_info=remove_symbols(product_in)

    return render_template('about.html',product_info=product_info,product_name=product_name)

@app.route('/review')
def review():
    product_name=session.get('productname')
    product_re = fetch_review(product_name)
    product_review=remove_symbols(product_re)
<<<<<<< HEAD
    product_re1 = fetch_review(product_name)
    product_review1=remove_symbols(product_re1)
    product_re2 = fetch_review1(product_name)
    product_review2=remove_symbols(product_re2)
    product_re3 = fetch_review(product_name)
    product_review3=remove_symbols(product_re3)
    product_re4 = fetch_review(product_name)
    product_review4=remove_symbols(product_re4)
    """product_re5 = fetch_review1(product_name)
    product_review5=remove_symbols(product_re5)
    product_re6 = fetch_review(product_name)
    product_review6=remove_symbols(product_re6)
    product_re7 = fetch_review(product_name)
    product_review7=remove_symbols(product_re7)
    product_re8 = fetch_review1(product_name)
    product_review8=remove_symbols(product_re8)"""
    """product_review5=product_review5,product_review6=product_review6,product_review7=product_review7,product_review8=product_review8"""
    return render_template('review.html',product_review=product_review,product_review1=product_review1,product_review2=product_review2,product_review3=product_review3,product_review4=product_review4,product_name=product_name)


def is_valid_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def fetch_logo_url(provider_name):
    
    specific_publishers = {
        "the times of india": "timesofindia.indiatimes.com",
        "the economic times": "economictimes.indiatimes.com",
        "times now": "timesnow.indiatimes.com",
        "mirror now": "mirrornow.indiatimes.com",
        "et brandequity": "brandequity.economictimes.indiatimes.com"
    }
    
   
    normalized_provider = provider_name.lower()

   
    if normalized_provider in specific_publishers:
        domain = specific_publishers[normalized_provider]
        clearbit_url = f"https://logo.clearbit.com/{domain}"
        if is_valid_url(clearbit_url):
            return clearbit_url
    
   
    domain_patterns = [
        '{}.com',
        '{}.in',
        '{}.co.in',
        '{}.org',
        '{}news.com',
        '{}.co',
        '{}.net',
        '{}.edu'
    ]
    
    provider_variants = [
        '-'.join(normalized_provider.split()),  
        ''.join(normalized_provider.split())   
    ]
    
  
    for pattern in domain_patterns:
        for variant in provider_variants:
            clearbit_url = f"https://logo.clearbit.com/{pattern.format(variant)}"
            if is_valid_url(clearbit_url):
                return clearbit_url
    
  
    fallback_domain = provider_variants[1]  
    google_favicon_url = f"https://www.google.com/s2/favicons?sz=64&domain={fallback_domain}.com"
    if is_valid_url(google_favicon_url):
        return google_favicon_url
    
   
    return "https://upload.wikimedia.org/wikipedia/commons/0/0b/Google_News_icon.png"


def get_google_news_rss(product):
    rss_url = f"https://news.google.com/rss/search?q={product}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    articles = []
    for entry in feed.entries:
        if len(articles) >= 5:
            break
    
        if '-' in entry.title:
            title_parts = entry.title.rsplit('-', 1)
            title = title_parts[0].strip()
            provider = title_parts[1].strip()
        else:
            title = entry.title.strip()
            provider = 'Unknown'
        
       
        logo_url = fetch_logo_url(provider)
        
        if logo_url:  
            articles.append({
                'provider': provider,
                'title': title,
                'url': entry.link,
                'date': entry.published,
                'logo_url': logo_url
            })
    
    return articles

=======

    return render_template('review.html',product_review=product_review,product_name=product_name)
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f

@app.route('/SocialTrends')
def Social_Trends():
    product_name=session.get('productname')
<<<<<<< HEAD
    prod = product_name  
    prod = prod.replace(' ', ',') 
    google_news = get_google_news_rss(prod)
    p1,p2,p3,p4 = fetch_social_trends(product_name)
    link1,link2,link3=fetch_youtube_videos(product_name)

    return render_template('Social_Trends.html',p1=p1,p2=p2,p3=p3,p4=p4,product_name=product_name,link1=link1,link2=link2,link3=link3, product_data=google_news, prod=prod)

product_data = {
    "Ahaglow Moisturizer, Acne control, cosmetics": {
        "products": [
            {
                "name": "Pond's Super Light Gel Oil Free Moisturiser",
                "description": "A lightweight, oil-free moisturizer that provides hydration without clogging pores.",
            },
            {
                "name": "Mamaearth Vitamin C Oil-Free Moisturizer",
                "description": "An oil-free moisturizer infused with vitamin C and fruit extracts.",
            },
            {
                "name": "Lakme Peach Milk Intense Moisturizer Lotion",
                "description": "A creamy moisturizer that nourishes and hydrates the skin.",
            },
            {
                "name": "Cetaphil Moisturising Lotion",
                "description": "A gentle, non-greasy moisturizer suitable for sensitive skin.",
            }
        ]
    },
    "Dove pink bar soap": {
        "products": [
            {
                "name": "Pears Soft & Fresh Soap Bar",
                "description": "A mild, glycerin-based soap that cleanses the skin without stripping its natural oils.",
            },
            {
                "name": "NIVEA Creme Soft Soap",
                "description": "A creamy soap that gently cleanses and moisturizes the skin.",
            },
            {
                "name": "Sheny Soft Soap Glowing",
                "description": "A soap that helps improve skin texture and radiance.",
            },
            {
                "name": "Lux International Creamy Perfection Soap",
                "description": "A luxurious soap that provides a rich, creamy lather.",
            },
            {
                "name": "Lifebuoy Neem and Aloe Vera Soap",
                "description": "A soap that combines the benefits of neem and aloe vera to cleanse and nourish the skin.",
            }
        ]
    },
    "Lakme Forever Matte Foundation": {
        "products": [
            {
                "name": "Maybelline New York Fit Me Matte+Poreless Liquid Foundation Tube",
                "description": "A liquid foundation that provides a natural, matte finish.",
            },
            {
                "name": "FACES CANADA All Day Hydra Matte Foundation",
                "description": "A long-lasting, hydrating foundation that gives a smooth, matte finish.",
            },
            {
                "name": "Dazller Moisturizing Liquid Makeup",
                "description": "A moisturizing foundation that provides a natural, matte finish.",
            },
            {
                "name": "MAC Studio Fix Professional Waterproof Foundation",
                "description": "A long-wearing, waterproof foundation that provides a matte finish.",
            },
            {
                "name": "Colorbar Xoxo Everlasting Foundation - Sand 004",
                "description": "A lightweight, buildable foundation that gives a natural, matte finish.",
            }
        ]
    },
    "Nivea Soft, Light Moisturizer": {
        "products": [
            {
                "name": "Dove Beauty Cream",
                "description": "A rich, creamy moisturizer that deeply nourishes and hydrates the skin.",
            },
            {
                "name": "Olay Moisturising Cream",
                "description": "A lightweight, non-greasy moisturizer that provides long-lasting hydration.",
            },
            {
                "name": "Neutriderm Moisturising Lotion",
                "description": "A gentle, non-comedogenic moisturizer suitable for sensitive skin.",
            },
            {
                "name": "Moisturizing Cream For Dry To Very Dry Skin",
                "description": "A deeply nourishing cream that helps replenish the skin's moisture levels.",
            },
            {
                "name": "Pond's Super Light Gel Oil Free Moisturiser",
                "description": "A lightweight, oil-free gel moisturizer that provides hydration.",
            }
        ]
    },
    "Oreo, biscuit": {
        "products": [
            {
                "name": "Britannia Hi-Fibre Digestive Biscuits",
                "description": "Digestive biscuits made with high-fiber ingredients.",
            },
            {
                "name": "Sunfeast Marie Light Biscuits",
                "description": "Light, airy biscuits with a delicate flavor.",
            },
            {
                "name": "Parle Hide Seek Black Bourbon Biscuits",
                "description": "Chocolate-flavored biscuits with a creamy filling.",
            },
            {
                "name": "Hide & Seek Parle Chocolate Chip Cookies",
                "description": "Cookies made with real chocolate chips for a delicious taste.",
            },
            {
                "name": "Britannia Milk Bikis Biscuits",
                "description": "Milk-flavored biscuits with a creamy taste.",
            }
        ]
    },
    "Pampers All Round Protection Pants": {
        "products": [
            {
                "name": "MamyPoko Tape Diapers for Premature Babies",
                "description": "Soft, comfortable diapers designed for premature babies.",
            },
            {
                "name": "Huggies Complete Comfort Wonder Pants",
                "description": "Breathable, stretchy diaper pants that offer a snug fit.",
            },
            {
                "name": "Himalaya Total Care Baby Pants Diapers",
                "description": "Organic, bamboo-based diaper pants that are gentle on sensitive skin.",
            },
            {
                "name": "Organic Bamboo Diapers",
                "description": "Eco-friendly diapers made from natural bamboo fibers.",
            },
            {
                "name": "Little Angel Baby Easy Dry Diaper Pants",
                "description": "Lightweight, easy-to-use diaper pants that provide reliable protection.",
            }
        ]
    }
}

def scrape_images(product_name):
    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={product_name.replace(' ', '+')}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')


    img_tags = soup.find_all('img')
    image_links = []


    for img in img_tags:
        img_url = img.get('src')
        if img_url and img_url.startswith('http'):
            image_links.append(img_url)

    return image_links

=======
    p1,p2,p3,p4 = fetch_social_trends(product_name)

    return render_template('Social_Trends.html',p1=p1,p2=p2,p3=p3,p4=p4,product_name=product_name)
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f

@app.route('/similar')
def similar():
    product_name=session.get('productname')
<<<<<<< HEAD
    products = product_data.get(product_name, {}).get("products", [])
    images_data = []

    for product in products:
        img_urls = scrape_images(product["name"])
        if img_urls:
            images_data.append({
                'name': product['name'],
                'description': product['description'],
                'image_url': img_urls[0]  
            })
    product_si = fetch_similar(product_name)
    product_similar=remove_symbols(product_si)

    return render_template('similar.html',product_similar=product_similar,product_name=product_name, images=images_data)

@app.route('/explore_product', methods=['POST'])
def explore_product():
    data = request.get_json()
    product_name = data.get('product_name')
    
    session['productname'] = product_name
  
    return redirect(url_for('service'))
=======
    product_si = fetch_similar(product_name)
    product_similar=remove_symbols(product_si)

    return render_template('similar.html',product_similar=product_similar,product_name=product_name)

>>>>>>> 21519aabe54663bd377341fc9c236730daab707f

@app.route('/project')
def project():
    return render_template('project.html')


@app.route("/get_response", methods=["POST"])
def get_response_route():
    user_message = request.json.get("message")
    
    try:
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=user_message,
            max_tokens=150,
            temperature=0.7,
        )

        fulfillment_text = response.generations[0].text.strip()

        return jsonify({"response": fulfillment_text})

    except Exception as e:
        return jsonify({"response": "Oops! Something went wrong. Please try again."}), 500


class_data_mapping = {
    "Ahaglow Moisturizer": "Ahaglow Moisturizer, Acne control, cosmetics",
    "Dove": "Dove pink bar soap",
    "Lakme Foundation": "Lakme Forever Matte Foundation",
    "Nivea Soft cream": "Nivea Soft, Light Moisturizer",
    "Oreo": "Oreo, biscuit",
    "Pampers": "Pampers All Round Protection Pants"
}


detected_object = None
detection_found = False
camera_active = False
cap = None

def initialize_camera():
    """Function to initialize the camera when the app starts."""
    global cap, camera_active
    cap = cv2.VideoCapture(0)
    camera_active = cap.isOpened()
    print(f"Camera active: {camera_active}") 


def activate_camera():
    """Function to activate the camera and perform detection."""
    global cap, detected_object, detection_found, camera_active

    if not camera_active:
        print("Error: Camera not initialized.")
        return

    while camera_active:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imwrite("frame.jpg", frame)

        prediction = model.predict("frame.jpg").json()
        detections = prediction['predictions']

        for detection in detections:
            class_name = detection['class']
            confidence = detection['confidence']

            if confidence >= 0.75:
                x = detection['x']  
                y = detection['y']  
                width = detection['width']
                height = detection['height']

                x1 = int(x - width / 2)
                y1 = int(y - height / 2)
                x2 = int(x + width / 2)
                y2 = int(y + height / 2)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{class_name} {confidence:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                detected_object = class_data_mapping.get(class_name, class_name)
                detection_found = True
                camera_active = False
                break

        if not camera_active:
            break

    cap.release()
    cv2.destroyAllWindows()

@app.route('/start_camera')
def start_camera():
    """Route to start the camera."""
    global detected_object, detection_found, camera_active
    detected_object = None
    detection_found = False

    if not camera_active:
        return jsonify({"status": "Camera not ready"}), 500

    threading.Thread(target=activate_camera).start()

    return jsonify({"status": "Camera started"})

@app.route('/video_feed')
def video_feed():
    """Video streaming route."""
    global cap
    if not cap or not camera_active:
        return Response(status=404)
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen():
    """Video streaming generator function."""
    global cap
    while camera_active:
        ret, frame = cap.read()
        if not ret:
            break
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    cap.release()

@app.route('/detect')
def detect():
    """Route to check detection results."""
    global detected_object, detection_found
    print(detected_object)
    if detection_found:
        product_name=detected_object
        session['productname'] = product_name
        return jsonify({"alert": f"Product detected: {detected_object}", "status": "success","redirect_url": url_for('service')})
       
    else:
        return jsonify({"alert": "No matching image detected", "status": "failure"})
<<<<<<< HEAD
    
def get_google_news_rss1(product):
    rss_url = f"https://news.google.com/rss/search?q={product}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    articles = []
    for entry in feed.entries:
        if len(articles) >= 2:
            break
       
        if '-' in entry.title:
            title_parts = entry.title.rsplit('-', 1)
            title = title_parts[0].strip()
            provider = title_parts[1].strip()
        else:
            title = entry.title.strip()
            provider = 'Unknown'
        
        logo_url = fetch_logo_url(provider)
        
        if logo_url:  
            articles.append({
                'provider': provider,
                'title': title,
                'url': entry.link,
                'date': entry.published,
                'logo_url': logo_url
            })
    
    return articles

=======
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f

@app.route('/service')
def service():
    """Route to render the service page after detection."""
    product_name = session.get('productname')
<<<<<<< HEAD
    prod = product_name  
    prod = prod.replace(' ', ',')  
    google_news = get_google_news_rss1(prod)
=======
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f
    if product_name:
        product_info = fetch_product_details(product_name)
        product_rating = fetch_product_rating(product_name)
        product_review = fetch_product_review(product_name)
        product_trends = fetch_product_trends(product_name)
        product_similar = fetch_product_similar(product_name)
<<<<<<< HEAD
        product_re6 = fetch_review(product_name)
        product_review6=remove_symbols(product_re6)
        product_re7 = fetch_review(product_name)
        product_review7=remove_symbols(product_re7)
        product_re8 = fetch_review1(product_name)
        product_review8=remove_symbols(product_re8)
        online_link = main(product_name)
        link1,link2,link3=fetch_youtube_videos(product_name)
=======
        online_link = main(product_name)
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f
        return render_template('service.html',
                               product_info=product_info,
                               product_name=product_name,
                               product_rating=product_rating,
                               product_review=product_review,
<<<<<<< HEAD
                               product_trends=product_trends,product_data=google_news, prod=prod,
                               product_similar=product_similar,online_link=online_link,product_review6=product_review6,product_review7=product_review7,product_review8=product_review8,link1=link1,link2=link2
                               )
    else:
        return "No product detected"

if __name__ == "__main__":
    initialize_camera()
    app.run(host='0.0.0.0', port=5000)
=======
                               product_trends=product_trends,
                               product_similar=product_similar,online_link=online_link)
    else:
        return "No product detected"
>>>>>>> 21519aabe54663bd377341fc9c236730daab707f
