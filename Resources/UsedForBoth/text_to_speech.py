# Jay Dadas


import pyttsx3

def sayAndWait(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()
