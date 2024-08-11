from gpiozero import Button
from signal import pause

# Create a Button object for each GPIO pin
buttons = [Button(pin) for pin in range(2, 28)]

# Define a function to be called when any button is pressed
def on_button_pressed(pin):
    print(f"Button on GPIO pin {pin} pressed")

# Attach the function to the when_pressed event for each button
for button in buttons:
    button.when_pressed = lambda button=button: on_button_pressed(button.pin.number)

# Keep the script running to continue detecting button presses
pause()
