import pyautogui  # For controlling mouse movements and clicks
from pynput import keyboard  # For listening to keyboard hotkeys
import time  # For sleep/delays when not clicking

# State flag to indicate whether autoclicker is active
running = False

# Callback invoked on any keyboard key press event
def on_start_press(key):
    global running
    # F2 starts the autoclicking loop
    if key == keyboard.Key.f2:
        print("Starting")
        running = True
    # F4 stops the autoclicking loop
    elif key == keyboard.Key.f4:
        print("Stopped")
        running = False

# Create a keyboard listener and give it the event handler
listener = keyboard.Listener(on_press=on_start_press)

# Start listener in background thread so we can continue to main loop
listener.start()

# Main program loop runs forever
while True:
    if running == True:
        # Perform a mouse click repeatedly with a short interval between clicks
        # This is the core autoclicker behavior.
        pyautogui.click(interval=0.01)
    else:
        # When not running, sleep briefly to avoid using 100% CPU.
        time.sleep(0.05)


