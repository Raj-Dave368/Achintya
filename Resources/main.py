# 🚩 Dada Ki Jay Ho 🚩


# Global Things ----------------------------------------
import speech_recognition as sr
import webbrowser as wb
import threading
import socket
import easyocr
import tkinter as tk
import pyperclip
import time

from tkinter.filedialog import askopenfilename
from Resources.Work_By_Raj.Opening_Applications import Opening_Applications
from Resources.Work_By_Raj.AutoSave import auto_save
from Resources.Work_By_Raj.Google_Calender_api.Resources import Return_events_info

from Resources.UsedForBoth import text_to_speech

from Resources.Work_By_Shaishav.Fetch_text_from_image import fetch_text_image
from Resources.Work_By_Shaishav import OpenFolder

recognizer = sr.Recognizer()
microphone = sr.Microphone()

recognizer.energy_threshold = 668
recognizer.pause_threshold = .6
recognizer.operation_timeout = 10


# -------------------------------------------------------


def welcome():
    text_to_speech.sayAndWait("Welcome Sir!")
    text_to_speech.sayAndWait("I am Your Virtual Assistant")
    # Return_events_info.say_event_details("how many events do I have today")


def run_cmd(cmd: str):
    cmd = cmd.lower()
    if "search" in cmd:
        thing_to_search = cmd[len("search "):]
        wb.open("https://www.google.com/search?q=" + thing_to_search)
    if "open " in cmd and "drive" not in cmd and "folder" not in cmd:
        try:
            Opening_Applications.open_applications(cmd)
        except Exception as e:
            text_to_speech.sayAndWait(e)
    if "open" in cmd and ("drive" in cmd or "folder" in cmd):
        OpenFolder.open_folder(cmd)
    if ("start" in cmd or "turn on" in cmd) and ("auto save" in cmd or "autosave" in cmd or "automatic save" in cmd):
        auto_save.is_auto_save_on = True
        thread = threading.Thread(target=auto_save.show_auto_save_window)
        thread.start()
        # auto_save.auto_save(cmd)
    if "upcoming" in cmd and "event" in cmd:
        text_to_speech.sayAndWait("Just wait Please")
        thread = threading.Thread(target=Return_events_info.say_event_details,
                                  args=("how many events do i have today",))
        thread.start()

    if 'fetch text from an image' in cmd or 'fetch text from image' in cmd or "get text from an image" in cmd or "get text from image" in cmd \
            or 'text from image' in cmd or 'text from an image' in cmd:
        thread = threading.Thread(target=fetch_text_image.fetch_text_from_image)
        thread.start()
def callback(recognizer, audio):
    # it can throw below error(s), so you have to handle it in your main.py or some other file whenever you call this function
    # sr.UnknownValueError
    # sr.RequestError
    try:
        text = recognizer.recognize_google(audio)
        print("CMD: " + text)
        thread = threading.Thread(target=run_cmd, args=(text,))
        thread.start()
    except sr.UnknownValueError as e:
        print("*" * 50)
        print("can not recognize")
        print(e)
        print("*" * 50)
    except sr.RequestError as e:
        text_to_speech.sayAndWait("No Internet Connection")
    except sr.WaitTimeoutError as e:
        print("*" * 50)
        text_to_speech.sayAndWait("Slow Internet Connection")
        print(e)
        print("*" * 50)
    except socket.timeout as e:
        text_to_speech.sayAndWait("Slow Internet Connection")
        print(e)


def ListenInBackground():
    print("You can speak now, we are listening in background")
    print("🚩 " * 36)

    stop_listening = recognizer.listen_in_background(microphone, callback, phrase_time_limit=5)
    # when stop_listening will call the recognizer will stop listening background

    while True:
        pass


welcome()
ListenInBackground()
