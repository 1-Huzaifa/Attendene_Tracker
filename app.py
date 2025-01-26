import os
from flask import Flask, request, jsonify
from deepface import DeepFace
 
app = Flask(__name__)
registered_faces_path = "registered_faces/"  # Folder containing registered faces
 
@app.route('/match', methods=['POST'])
def match_faces():
    try:
        # Save the incoming image
        incoming_image = request.files['image']
        incoming_image_path = "temp_incoming_image.jpg"
        incoming_image.save(incoming_image_path)
 
        # Iterate through the registered faces
        for person in os.listdir(registered_faces_path):
            person_folder = os.path.join(registered_faces_path, person)
            for face in os.listdir(person_folder):
                registered_face_path = os.path.join(person_folder, face)
                
                # Compare the incoming image with the registered face
                result = DeepFace.verify(
                    img1_path=incoming_image_path,
                    img2_path=registered_face_path
                )
                
                # If a match is found
                if result["verified"]:
                    return jsonify({
                        "message": f"Face matched with {person}",
                        "distance": result["distance"]
                    })
 
        return jsonify({"message": "No match found"})
 
    except Exception as e:
        return jsonify({"error": str(e)}), 400
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)