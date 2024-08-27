'''
In case you run into a case where you need to use a task-scheduler-like process to run keyboards command to run an automated program to avoid buying a premium license.
'''

import pyautogui
import os

def main ():

    pyautogui.hotkey('keystrokes')

    pyautogui.write('keystrokes')

    pyautogui.hotkey('keystrokes')

if __name__ == "__main__":
    main()
