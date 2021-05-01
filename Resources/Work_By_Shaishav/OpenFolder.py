# 🚩 Dada Ki Jay Ho 🚩


import os
import webbrowser

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
            cmd = cmd.replace("folder", "")
            folder_name = cmd[5:].strip()
            path += folder_name + "/"
            if os.path.isdir(path):
                webbrowser.open(path)
        print(path)


