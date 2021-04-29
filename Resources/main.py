# 🚩 Dada Ki Jay Ho 🚩



# Global Things ----------------------------------------
import speech_recognition as sr
import pyttsx3
from Resources.Work_By_Raj.Opening_Applications import Opening_Applications
from Resources.Work_By_Raj.AutoSave import auto_save
import threading
import socket
from Resources.UsedForBoth import text_to_speech

from Resources.Work_By_Shaishav.Fetch_text_from_image import fetch_text_image

recognizer = sr.Recognizer()
microphone = sr.Microphone()


recognizer.energy_threshold = 168
recognizer.pause_threshold = .6
recognizer.operation_timeout = 10
# -------------------------------------------------------


def run_cmd(cmd:str):
    cmd = cmd.lower()
    if "open" in cmd:
        try:
            Opening_Applications.open_applications(cmd)
        except Exception as e:
            text_to_speech.sayAndWait(e)
    if "start" in cmd and ("auto save" in cmd or "autosave" in cmd or "automatic save" in cmd):
        auto_save.is_auto_save_on = True
        thread = threading.Thread(target=auto_save.auto_save,args=(cmd,))
        thread.start()
    if "stop" in cmd and ("auto save" in cmd or "autosave" in cmd or "automatic save" in cmd):
        auto_save.is_auto_save_on = False
    if 'fetch text from an image' in cmd or 'fetch text from image' in cmd or "get text from an image" in cmd or  "get text from image" in cmd:
        fetch_text_image.fetch_text_from_image(cmd)





def callback(recognizer, audio):
    # it can throw below error(s), so you have to handle it in your main.py or some other file whenever you call this function
    # sr.UnknownValueError
    # sr.RequestError
    try:
        text = recognizer.recognize_google(audio)
        print("CMD: "+text)
        # TODO: Use Thread here for calling run_cmd(cmd)
        run_cmd(text)

    except sr.UnknownValueError as e:
        print("*"*50)
        print("can not recognize")
        print(e)
        print("*" * 50)
    except sr.RequestError as e:
        text_to_speech.sayAndWait("No Internet Connection")
    except sr.WaitTimeoutError as e:
        print("*"*50)
        text_to_speech.sayAndWait("Slow Internet Connection")
        print(e)
        print("*" * 50)
    except socket.timeout as e:
        text_to_speech.sayAndWait("Slow Internet Connection")
        print(e)


def ListenInBackground():
    print("You can speak now, we are listening in background")

    stop_listening = recognizer.listen_in_background(microphone, callback)
    # when stop_listening will call the recognizer will stop listening background
    while True:
        pass


def Listen():
    with microphone as mic:
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio)
        return text


def run():
    while True:
        try:
            cmd = Listen()
            print(cmd)
            if cmd:
                run_cmd(cmd)
        except Exception as e:
            print(e)


# ListenInBackground()

run_cmd("fetch text from an image")

