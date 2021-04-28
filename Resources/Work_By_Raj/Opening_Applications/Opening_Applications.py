# jay Dada



import os


def open_applications(cmd: str):
    if "open" not in cmd:
        txt_to_speech(txt="Not Able to Open An Application")
    try:
        if "chrome" in cmd:
            os.system("start chrome")
        elif "edge" in cmd:
            os.system("start msedge")
        elif "word" in cmd:
            os.system("start winword")
        elif "powerpoint" in cmd or "power point" in cmd:
            os.system("start powerpnt")
        elif "vs code" in cmd or "code" in cmd:
            os.system("start code")
        elif "task manager" in cmd:
            os.system("start Taskmgr")
        elif "calculator" in cmd:
            os.system("start calc")
        elif "excel" in cmd:
            os.system("start excel")
        elif "files" in cmd or "file explorer" in cmd or "explorer" in cmd:
            os.system("start explorer")
        elif "notepad" in cmd:
            os.system("start notepad")
        else:
            raise Exception("Not Able To Open an Application, Sorry!")
    except:
        raise Exception("Not Able To Open an Application, Sorry!")



if __name__ == '__main__':
    open_applications("open excel")

