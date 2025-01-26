from deepface import DeepFace
import os
img_path_1 = os.path.join(os.getcwd(),"registered_face\mustafa.jpeg")
img_path_2 = os.path.join(os.getcwd(),"testing_face\mustafa2.jpeg")
print(img_path_1)
print(img_path_2)


result = DeepFace.verify(img1_path="mustafa.jpeg",img2_path="hozefa.jpeg")

print(result)