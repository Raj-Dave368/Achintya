# jay Dada


# Global Things ----------------------------------------
import speech_recognition as sr


recognizer = sr.Recognizer()
microphone = sr.Microphone()


recognizer.pause_threshold = .7
# -------------------------------------------------------

def ListenCommand()->str:
    # it can throw below error(s), so you have to handle it in your main.py or some other file whenever you call this function
    # sr.UnknownValueError
    print("You can speek now")

    with microphone as mic:
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio)
        print(text)
        return text
    
ListenCommand()
    

    