import cv2
from google.cloud import vision
from google.cloud.vision_v1 import types
import os
import pyttsx3

# Set the environment variable to specify the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/location/path/filename.json"

# Set up Google Cloud Vision API client
client = vision.ImageAnnotatorClient()


# Function to perform object detection on an image
def object_detection_from_image(image_path):
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.object_localization(image=image)
    objects = response.localized_object_annotations

    if objects:
        return [obj.name for obj in objects]
    else:
        return []


# Function to capture image from camera
def capture_image(camera_index=0, image_path="image.jpg"):
    camera = cv2.VideoCapture(camera_index)
    _, image = camera.read()
    cv2.imwrite(image_path, image)
    camera.release()


# Function to delete the image
def delete_image(image_path):
    os.remove(image_path)


# Function to say the detected objects
def say_detected_objects(objects):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say("I see the following objects:")
    for obj in objects:
        engine.say(obj)
    engine.runAndWait()


# Main function
def main():
    image_path = "image.jpg"
    capture_image(image_path=image_path)
    detected_objects = object_detection_from_image(image_path)
    print("Detected objects:")
    print(detected_objects)
    if detected_objects:
        say_detected_objects(detected_objects)
    delete_image(image_path)


if __name__ == "__main__":
    main()
