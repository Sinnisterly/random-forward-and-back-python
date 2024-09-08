import random
import time
import pyautogui
import keyboard
import ctypes

# Hide the console window
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def navigate_forward():
    """Simulate pressing the forward button (Alt + Right Arrow)"""
    keyboard.press_and_release('alt+right')

def navigate_back():
    """Simulate pressing the back button (Alt + Left Arrow)"""
    keyboard.press_and_release('alt+left')

def random_delay():
    """Generate a random delay between 1-60 minutes."""
    return random.randint(1, 60) * 60  # convert minutes to seconds

while True:
    delay = random_delay()
    time.sleep(delay)
    
    if random.random() < 0.07:  # 7% chance of navigating forward
        navigate_forward()
    else:
        navigate_back()
    
    if keyboard.is_pressed('end'):  # exit script when END key is pressed
        break