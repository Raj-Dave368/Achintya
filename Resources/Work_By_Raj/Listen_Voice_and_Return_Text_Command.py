# jay Dada


# Global Things ----------------------------------------
import speech_recognition as sr


recognizer = sr.Recognizer()
microphone = sr.Microphone()


recognizer.pause_threshold = .7
recognizer.operation_timeout = 15
# -------------------------------------------------------


def ListenCommand()->str:
    # it can throw below error(s), so you have to handle it in your main.py or some other file whenever you call this function
    # sr.UnknownValueError
    # sr.RequestError 
    print("You can speak now")

    with microphone as mic:
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio)
        print(text)
        return text
    

def callback(recognizer, audio):
    text = recognizer.recognize_google(audio)
    print(text)


def ListenInBackground():
    # it can throw below error(s), so you have to handle it in your main.py or some other file whenever you call this function
    # sr.UnknownValueError
    # sr.RequestError
    print("You can speak now, we are listening in background")

    stop_listening = recognizer.listen_in_background(microphone, callback)
    # when stop_listening will call the recognizer will stop listening background
    while True:
        pass


ListenInBackground()
