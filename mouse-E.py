import pyautogui
import time
import subprocess

# Function to get idle time in seconds (macOS)
def get_idle_duration():
    cmd = 'ioreg -c IOHIDSystem | awk \'/HIDIdleTime/ {print int($NF/1000000000)}\''
    idle_time = subprocess.check_output(cmd, shell=True)
    return int(idle_time)

# Function to move the mouse slightly
def move_mouse():
    x, y = pyautogui.position()  # Get the current mouse position
    pyautogui.moveTo(x + 1, y + 1)  # Move the mouse slightly
    pyautogui.moveTo(x, y)  # Move it back

idle_time_limit = 10  # 5 minutes in seconds

while True:
    idle_time = get_idle_duration()
    if idle_time >= idle_time_limit:
        move_mouse()  # Move mouse after 5 minutes of inactivity
        time.sleep(60)  # Wait for 1 minute before the next movement
    else:
        time.sleep(10)  # Check again after 10 seconds
