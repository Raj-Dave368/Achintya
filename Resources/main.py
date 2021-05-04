# 🚩 Dada Ki Jay Ho 🚩


# Global Things ----------------------------------------
import speech_recognition as sr
import webbrowser as wb
import threading
import pyautogui
import datetime
import socket
import os

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
recognizer.operation_timeout = 11


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
    if "turn off computer" in cmd or "switch off" in cmd:
        os.system("shutdown /s /t 1")

    if 'fetch text from an image' in cmd or 'fetch text from image' in cmd or "get text from an image" in cmd or "get text from image" in cmd \
            or 'text from image' in cmd or 'text from an image' in cmd:
        thread = threading.Thread(target=fetch_text_image.fetch_text_from_image)
        thread.start()

    if "take a screen shot" in cmd or "take screen shot" in cmd or "take a screenshot" in cmd or "take screenshot" in cmd:
        pyautogui.screenshot(f"C://users//rajda//Desktop//{str(datetime.datetime.now()).replace(':','-')}.jpg")

# def callback(recognizer, audio):
#
#     # it can throw below error(s), so you have to handle it in your main.py or some other file whenever you call this function
#     # sr.UnknownValueError
#     # sr.RequestError
#     try:
#         text = recognizer.recognize_google(audio)
#         print("CMD: " + text)
#         thread = threading.Thread(target=run_cmd, args=(text,))
#         thread.start()
#     except sr.UnknownValueError as e:
#         print("*" * 50)
#         print("can not recognize")
#         print(e)
#         print("*" * 50)
#     except sr.RequestError as e:
#         text_to_speech.sayAndWait("No Internet Connection")
#     except sr.WaitTimeoutError as e:
#         print("*" * 50)
#         text_to_speech.sayAndWait("Slow Internet Connection")
#         print(e)
#         print("*" * 50)
#     except socket.timeout as e:
#         text_to_speech.sayAndWait("Slow Internet Connection")
#         print(e)
#
#
# def ListenInBackground():
#     print("You can speak now, we are listening in background")
#     print("🚩 " * 36)
#     thread = threading.Thread(target=lambda : frame.mainloop)
#     thread.start()
#
#     stop_listening = recognizer.listen_in_background(microphone, callback, phrase_time_limit=5)
#     # when stop_listening will call the recognizer will stop listening background
#
#     while True:
#         pass


from pynput import keyboard
from plyer import notification

def listen():
    with microphone as mic:
        print("You can speak now, we are listening in background")
        print("🚩 " * 36)
        notification.notify("Listening ...", "You can speak now ...", timeout=1, toast=True)
        audio = recognizer.listen(mic, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio)
            print("CMD: " + text)
            notification.notify("CMD:... ", text, timeout=1.2)
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

thread = threading.Thread(target=listen)
def on_press(i):
    thread.isDaemon()
    print(i)
    print(dir(i))
    print(str(type(i)) == "<enum 'Key'>")
    if str(type(i)) == "<enum 'Key'>" and i.name == "esc":
        thread.start()

text_to_speech.sayAndWait("Hello Sir!")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


# with microphone as mic:
#     while True:
#         print("You can speak now, we are listening in background")
#         print("🚩 " * 36)
#         audio = recognizer.listen(mic, phrase_time_limit=5)
#         try:
#             text = recognizer.recognize_google(audio)
#             print("CMD: " + text)
#             thread = threading.Thread(target=run_cmd, args=(text,))
#             thread.start()
#         except sr.UnknownValueError as e:
#             print("*" * 50)
#             print("can not recognize")
#             print(e)
#             print("*" * 50)
#         except sr.RequestError as e:
#             text_to_speech.sayAndWait("No Internet Connection")
#         except sr.WaitTimeoutError as e:
#             print("*" * 50)
#             text_to_speech.sayAndWait("Slow Internet Connection")
#             print(e)
#             print("*" * 50)
#         except socket.timeout as e:
#             text_to_speech.sayAndWait("Slow Internet Connection")
#             print(e)

# welcome()

