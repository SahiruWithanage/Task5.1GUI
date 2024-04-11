import tkinter as tk
import RPi.GPIO as GPIO

# Set GPIO mode to standard BOARD numbering
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins for LEDs
RED_PIN = 11
GREEN_PIN = 12
BLUE_PIN = 13

# Initialize GPIO pins for LEDs
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Function to control LEDs based on radio button selection
def light_led():
    selected_led = var.get()
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)
    if selected_led == 1:
        GPIO.output(RED_PIN, GPIO.HIGH)
    elif selected_led == 2:
        GPIO.output(GREEN_PIN, GPIO.HIGH)
    elif selected_led == 3:
        GPIO.output(BLUE_PIN, GPIO.HIGH)

# Create GUI window
root = tk.Tk()
root.title("LED Control")

# Create radio buttons
var = tk.IntVar()
tk.Radiobutton(root, text="Red", variable=var, value=1, command=light_led).pack(anchor=tk.W)
tk.Radiobutton(root, text="Green", variable=var, value=2, command=light_led).pack(anchor=tk.W)
tk.Radiobutton(root, text="Blue", variable=var, value=3, command=light_led).pack(anchor=tk.W)

# Run the GUI
root.mainloop()

# Cleanup GPIO
GPIO.cleanup()