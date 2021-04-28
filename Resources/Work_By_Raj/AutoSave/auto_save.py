# maro mahakal



import keyboard
import pyautogui
import win32gui
import time

def auto_save(cmd:str):
    if "auto save" in cmd or "autosave" in cmd or "automatic save" in cmd:
        if "- Word" in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            keyboard.release('alt')  # alt key ne release karo
            keyboard.press_and_release('esc')  # jo alt key press hase and release thase to eno
            keyboard.release('shift')
            keyboard.press_and_release('esc')
            # matlab ke -> alt key press ek var press_release thay, to je File,Edit... vala menu hoy 6 te na par focus jase (ek var
            # alt key press kari ne jo shu thay MS word ma) to te effect ne remove karva mate esc no use thay etle alt ne release karine
            # tarat j aapde esc ne press_release karavi dai A 6i A
            keyboard.block_key('alt')  # during ctrl+s, alt ne block kari A 6i A
            keyboard.block_key('shift')  # during ctrl+s, shift ne block kari A 6i A
            print("key is blocked")
            pyautogui.hotkey('ctrl', 's') # here the actual work
            time.sleep(1)
            keyboard.release('alt')  # releasing alt
            keyboard.release('shift')  # releasing shift
            print("key is released")
            print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
