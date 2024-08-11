from gpiozero import Button
import subprocess
import time
import pyttsx3
import socket

# Initialize Text to Speech engine
engine = pyttsx3.init()

# Define button pins
button1 = Button(26)
button2 = Button(19)
button3 = Button(21)
button4 = Button(24)
button5 = Button(27)

# Define commands corresponding to buttons
commands = {
    button1: ("/home/sightsense/Desktop/sys-env/bin/python", "/home/sightsense/Desktop/codeBase/ocr.py"),
    button2: ("/home/sightsense/Desktop/sys-env/bin/python", "/home/sightsense/Desktop/codeBase/obj.py"),
    button3: ("/home/sightsense/Desktop/sys-env/bin/python", "/home/sightsense/Desktop/codeBase/jarviseng.py"),
    button4: ("/home/sightsense/Desktop/sys-env/bin/python", "/home/sightsense/Desktop/codeBase/obs/tf-lite-object_det/test.py"),
    button5: ("/home/sightsense/Desktop/sys-env/bin/python", "/home/sightsense/Desktop/codeBase/jarviseng.py")
}

# Function to run command when a button is pressed
def run_command(command):
    subprocess.run(command, shell=False)  # Using shell=False to prevent command injection

# Function to say the given message
def speak(message):
    print(message)
    engine.say(message)
    engine.runAndWait()

# Function to check internet connectivity
def check_internet():
    try:
        # Check if it's possible to resolve a known external domain name
        host = socket.gethostbyname("www.google.com")
        # If successful, return True (internet connection exists)
        return True
    except socket.error:
        # If an error occurs, return False (no internet connection)
        return False

# Function to handle button press event with debounce
def handle_button_press(button):
    # Implementing debounce
    time.sleep(0.1)  # Wait for 200ms
    if button.is_pressed:
        if button == button1:
            message = "OCR is activated"
        elif button == button2:
            message = "Object Detection is activated"
        elif button == button3:
            message = "AI Assistant is activated"
        elif button == button4:
            message = "Obstacle Detection is activated"
        elif button == button5:
            message = "Ai Assistant is activated, Start speaking in the next 5 seconds"
        else:
            message = " "
        
        print(message)
        engine.say(message)
        engine.runAndWait()
        
        run_command(commands[button])

# Assign the corresponding command to each button press event
button1.when_pressed = lambda: handle_button_press(button1)
button2.when_pressed = lambda: handle_button_press(button2)
button3.when_pressed = lambda: handle_button_press(button3)
button4.when_pressed = lambda: handle_button_press(button4)
button5.when_pressed = lambda: handle_button_press(button5)

try:
    # Say "system has booted"
    speak("System has booted")

    # Check for internet connectivity
    internet_connected = check_internet()
    if internet_connected:
        speak("Network connected")
    else:
        # Wait for 2 minutes for network connection
        time.sleep(60)
        internet_connected = check_internet()
        if not internet_connected:
            speak("Please connect to the internet")
            # Further wait for another minute
            time.sleep(10)
            internet_connected = check_internet()
            if not internet_connected:
                speak("Please connect to the internet")

    # Keep the script running
    while True:
        time.sleep(0.1)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    # Clean up GPIO resources
    pass
finally:
    button1.close()
    button2.close()
    button3.close()
    button4.close()
    button5.close()