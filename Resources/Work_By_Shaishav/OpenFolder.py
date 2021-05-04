# 🚩 Dada Ki Jay Ho 🚩


import os
import webbrowser
from Resources.UsedForBoth.text_to_speech import sayAndWait

path = ""
def open_folder(cmd:str):
    global path
    if "open" in cmd and ("folder" in cmd or "drive" in cmd):

        if "drive" in cmd:
            cmd = cmd.replace("drive", "")
            drive_name = cmd[5:].strip()
            path = ""
            path += drive_name + ":/"
            if os.path.isdir(path):
                webbrowser.open(path)
            else:
                sayAndWait("No such drive is available")
        else:
            cmd = cmd.replace("folder", "")
            folder_name = cmd[5:].strip()
            path += folder_name + "/"
            if os.path.isdir(path):
                webbrowser.open(path)
            else:
               sayAndWait("No such folder is available")
        print(path)


