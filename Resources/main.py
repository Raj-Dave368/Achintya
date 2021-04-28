# 🚩 Dada Ki Jay Ho 🚩



# Global Things ----------------------------------------
import speech_recognition as sr
import pyttsx3
from Resources.Work_By_Raj.Opening_Applications import Opening_Applications
from Resources.Work_By_Raj.AutoSave import auto_save
import threading

engine = pyttsx3.init()

recognizer = sr.Recognizer()
microphone = sr.Microphone()

recognizer.energy_threshold = 168
recognizer.pause_threshold = .6
recognizer.operation_timeout = 15
# -------------------------------------------------------


def sayAndWait(txt):
    engine.say(txt)
    engine.runAndWait()


def run_cmd(cmd:str):
    cmd = cmd.lower()
    if "open" in cmd:
        try:
            Opening_Applications.open_applications(cmd)
        except Exception as e:
            if engine._inLoop:
                engine.endLoop()
            threading.Thread(target=sayAndWait, args=(e,)).start()
            # sayAndWait(e)
    if "auto save" in cmd or "autosave" in cmd or "automatic save" in cmd:
        auto_save.auto_save(cmd)




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
        print("e")
        print("*" * 50)
    except sr.RequestError as e:
        sayAndWait("No Internet Connection")
    except sr.WaitTimeoutError as e:
        print("*"*50)
        sayAndWait("Slow Internet Connection")
        print("e")
        print("*" * 50)


def ListenInBackground():
    print("You can speak now, we are listening in background")

    stop_listening = recognizer.listen_in_background(microphone, callback)
    # when stop_listening will call the recognizer will stop listening background
    while True:
        pass


ListenInBackground()

