# Jay Dada


import pyttsx3


def txt_to_speech(txt: str):
    engine = pyttsx3.init()
    print(txt)
    engine.say(txt)
    engine.runAndWait()
