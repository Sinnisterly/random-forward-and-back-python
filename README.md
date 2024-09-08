

# Random Web Navigation Automation Script

This Python script simulates random forward and backward navigation in a web browser. It runs indefinitely, making periodic random navigation actions, and stops only when the `END` key is pressed. The script is designed for Windows and hides its console window upon execution.

## Features

- **Random Navigation**: 
  - Simulates pressing `Alt + Right Arrow` (forward) or `Alt + Left Arrow` (backward) at random intervals.
  - The script decides to either navigate forward or backward with a 7% chance for forward navigation.
  
- **Random Delay**: 
  - The script introduces a random delay between 1 and 60 minutes before each navigation action.
  
- **Hidden Console Window**: 
  - Upon execution, the console window is hidden, running silently in the background.
  
- **Termination**: 
  - Press the `END` key to stop the script.

## Requirements

- Python 3.x
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [Keyboard](https://github.com/boppreh/keyboard)
  
To install the required dependencies, run:
```bash
pip install pyautogui keyboard
```

## How It Works

1. **Hiding the Console**: The script uses the `ctypes` library to hide the console window on Windows by calling Windows API functions.
  
2. **Random Delay Calculation**: After each navigation action, a random delay is generated between 1 to 60 minutes. The delay is calculated by generating a random integer between 1 and 60, then converting it into seconds.

3. **Random Navigation**: The script has a 7% chance of pressing `Alt + Right Arrow` (navigate forward), otherwise, it presses `Alt + Left Arrow` (navigate backward).

4. **Termination**: The script listens for the `END` key. Once this key is pressed, the script exits.

## How to Use

1. Clone the repository or download the script.

2. Install the required Python packages with `pip`.

3. Run the script using Python:
   ```bash
   python scriptnamehere.py
   ```
4. The script will start navigating randomly in your browser. To stop it, press the `END` key.

## Important Notes

- The script relies on PyAutoGUI and keyboard modules, which are designed for automating keyboard input. Ensure that the browser window is active for the script to perform the navigation.
- The script is designed for Windows, and hiding the console might not work on other operating systems.

