import pyautogui
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.F1:
        print("Started auto-clicking. F2 to stop.")
        while True:
            pyautogui.click(button="left")
            

