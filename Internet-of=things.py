import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # Pin 11 as output for controlling a relay (for example, to control a light)

# Function to toggle the relay
def toggle_relay():
    GPIO.output(11, not GPIO.input(11))  # Toggle the state of the relay
    print("Relay toggled")

try:
    while True:
        # Read input from user
        user_input = input("Press 't' to toggle the relay, or 'q' to quit: ")

        # Toggle relay if 't' is pressed
        if user_input == 't':
            toggle_relay()

        # Exit if 'q' is pressed
        elif user_input == 'q':
            break

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO
    GPIO.cleanup()
