from flask import Flask, render_template, Response,jsonify,request,session,url_for,send_from_directory
import cohere
from  roboflow import Roboflow
import cv2
from flask import Response, jsonify
import threading
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

    return render_template('review.html',product_review=product_review,product_name=product_name)

@app.route('/SocialTrends')
def Social_Trends():
    product_name=session.get('productname')
    p1,p2,p3,p4 = fetch_social_trends(product_name)

    return render_template('Social_Trends.html',p1=p1,p2=p2,p3=p3,p4=p4,product_name=product_name)

@app.route('/similar')
def similar():
    product_name=session.get('productname')
    product_si = fetch_similar(product_name)
    product_similar=remove_symbols(product_si)

    return render_template('similar.html',product_similar=product_similar,product_name=product_name)


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

@app.route('/service')
def service():
    """Route to render the service page after detection."""
    product_name = session.get('productname')
    if product_name:
        product_info = fetch_product_details(product_name)
        product_rating = fetch_product_rating(product_name)
        product_review = fetch_product_review(product_name)
        product_trends = fetch_product_trends(product_name)
        product_similar = fetch_product_similar(product_name)
        online_link = main(product_name)
        return render_template('service.html',
                               product_info=product_info,
                               product_name=product_name,
                               product_rating=product_rating,
                               product_review=product_review,
                               product_trends=product_trends,
                               product_similar=product_similar,online_link=online_link)
    else:
        return "No product detected"
