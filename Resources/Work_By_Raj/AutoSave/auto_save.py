# maro mahakal



import keyboard
import threading
import pyautogui
import win32gui
import time
from tkinter import *
from tkinter.ttk import *
from PIL import Image
from PIL import ImageTk

from Resources.UsedForBoth import text_to_speech



is_auto_save_on = False


def start_func():
    global  is_auto_save_on
    is_auto_save_on = True
    thread = threading.Thread(target=auto_save)
    thread.start()


def stop_func():
    global  is_auto_save_on
    is_auto_save_on = False
    if not is_auto_save_on: text_to_speech.sayAndWait("Auto Saver Stopped")


def auto_save():
    if is_auto_save_on: text_to_speech.sayAndWait("Hey, Starting Auto Saver")
    while is_auto_save_on:
        # keyboard.release('alt')  # alt key ne release karo
        # keyboard.press_and_release('esc')  # jo alt key press hase and release thase to eno
        # keyboard.release('shift')
        # keyboard.press_and_release('esc')
        # matlab ke -> alt key press ek var press_release thay, to je File,Edit... vala menu hoy 6 te na par focus jase (ek var
        # alt key press kari ne jo shu thay MS word ma) to te effect ne remove karva mate esc no use thay etle alt ne release karine
        # tarat j aapde esc ne press_release karavi dai A 6i A
        # keyboard.block_key('alt')  # during ctrl+s, alt ne block kari A 6i A
        # keyboard.block_key('shift')  # during ctrl+s, shift ne block kari A 6i A
        # print("key is blocked")
        pyautogui.hotkey('ctrl', 's')  # here the actual work
        time.sleep(8)
        # keyboard.release('alt')  # releasing alt
        # keyboard.release('shift')  # releasing shift
        # print("key is released")
        print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))



def show_auto_save_window():
    # creating tkinter window
    root = Tk()
    # Adding widgets to the root window

    # Creating a photoimage object to use image
    photo1 = Image.open(r"C:\Users\rajda\Downloads\start.png")
    photo1 = photo1.resize((200,168), Image.ANTIALIAS)
    photo2 = Image.open(r"C:\Users\rajda\Downloads\stop.png")
    photo2 = photo2.resize((200,168), Image.ANTIALIAS)

    photo1 = ImageTk.PhotoImage(photo1)
    photo2 = ImageTk.PhotoImage(photo2)

    # here, image option is used to
    # set image on button

    Label(root, text='AutoSave', font=(
        'Verdana', 15)).grid(row=0,column=1)
    Button(root, text='Click Me !', image=photo1, command=start_func).grid(row=1, column=0)
    Button(root, text='Click Me !', image=photo2, command=stop_func).grid(row=1, column=2)

    mainloop()
