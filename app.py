import os
from flask import Flask, request, jsonify , Response
#from deepface import DeepFace
from flask_cors import CORS
import numpy as np
import cv2
app = Flask(__name__)
CORS(app)
#registered_faces_path = "registered_faces/"  # Folder containing registered faces
 
#@app.route('/match', methods=['POST'])
#def match_faces():
#    try:
        # Save the incoming image
#        incoming_image = request.files['image']
#        incoming_image_path = "temp_incoming_image.jpg"
#        incoming_image.save(incoming_image_path)

        
        # Iterate through the registered faces
#        for person in os.listdir(registered_faces_path):
#            person_folder = os.path.join(registered_faces_path, person)
#            for face in os.listdir(person_folder):
#                registered_face_path = os.path.join(person_folder, face)
                
                # Compare the incoming image with the registered face
#                result = DeepFace.verify(
#                    img1_path=incoming_image_path,
#                    img2_path=registered_face_path
#                )
                
                # If a match is found
#                if result["verified"]:
#                    return jsonify({
#                        "message": f"Face matched with {person}",#
#                        "distance": result["distance"]
#                    })
 
#        return jsonify({"message": "No match found"})
 
 #   except Exception as e:
 #       return jsonify({"error": str(e)}), 400
 
@app.route('/',methods=['POST'])
def greet():
    data = request.get_json()
    if not data:
        return jsonify({"error":"Something Gone Wrong"}), 400

    lat =data.get('lats',"Unknown")
    long =data.get('longs', "Unknown")
    print(f"{lat} is {long} years old")
    
    return jsonify({"message":f" Recieved Successfully at Back end {lat}","Lattitude":lat , "longitude":long }) , 200



@app.route("/upload", methods=["POST"])
def upload_file():
    
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
 
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
 
    # Read the image file into memory
    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
 
    # Optional: process the image (e.g., convert to grayscale)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    # Convert the processed image back to bytes for display
    _, buffer = cv2.imencode(".jpg", image)
    response = Response(buffer.tobytes(), content_type="image/jpeg")
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
