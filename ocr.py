import cv2
from google.cloud import vision
from google.cloud.vision_v1 import types
import os
import pyttsx3

# Set the environment variable to specify the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/location/path/filename.json"

# Set up Google Cloud Vision API client
client = vision.ImageAnnotatorClient()


# Function to perform OCR on an image
def ocr_from_image(image_path):
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    else:
        return "No text found."


# Function to capture image from camera
def capture_image(camera_index=0, image_path="image.jpg"):
    camera = cv2.VideoCapture(camera_index)
    _, image = camera.read()
    cv2.imwrite(image_path, image)
    camera.release()


# Function to delete the image
def delete_image(image_path):
    os.remove(image_path)

def say_detected_objects(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)

    engine.runAndWait()
# Main function
def main():
    image_path = "image.jpg"
    capture_image(image_path=image_path)
    text = ocr_from_image(image_path)
    print("Text detected:")
    print(text)
    say_detected_objects(text)
    delete_image(image_path)



if __name__ == "__main__":
    main()
