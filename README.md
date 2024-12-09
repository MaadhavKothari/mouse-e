# mouse-e
e-mouse for mundane tasks
# Mouse-E: A Simple Mouse Mover Script

Mouse-E is a lightweight Python script designed to simulate mouse activity on macOS. It prevents your computer from entering sleep or idle mode by moving the mouse slightly after a specified period of inactivity.

## Features

- Detects user inactivity using macOS `ioreg` command.
- Moves the mouse slightly to simulate activity.
- Customizable idle time limit and frequency of movement.

## Prerequisites

- Python 3.6 or later
- `pyautogui` library
- macOS environment

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mouse-e.git
   cd mouse-e
   ```

2. Install the required Python library:
   ```bash
   pip install pyautogui
   ```

## Usage

1. Open the script in a text editor to customize the idle time limit (in seconds). The default is `10` seconds:
   ```python
   idle_time_limit = 10
   ```

2. Run the script:
   ```bash
   python mouse-e.py
   ```

The script will monitor your system's idle time. If it exceeds the specified limit, the mouse will move slightly to prevent the system from registering inactivity.

## Notes

- **MacOS Only**: This script uses the `ioreg` command to detect idle time, which is specific to macOS.
- **Permissions**: Ensure you have the necessary permissions to execute the script and interact with system events.

## Customization

- Modify the `idle_time_limit` variable to change the inactivity threshold.
- Adjust the sleep intervals (`time.sleep(...)`) for checking idle status or movement frequency.

## Disclaimer

Use this script responsibly. It is intended for personal use to prevent unintended screen locking or system sleep. Ensure compliance with your organization's IT policies if used in a work environment.

---

