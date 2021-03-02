# oMNS


import pyautogui
import datetime

# scrrenshot -> its take a screenshot and save it we provide path as an argument, the file name must required proper format


def take_screenshot(cmd):
    if "screenshot" in cmd or "screen shot" in cmd:
        if "with name" in cmd:
            index_of_with_name = cmd.index("with name")
            index_after_adding_10= index_of_with_name + 10 
           
            name = cmd[index_after_adding_10: ]
            pyautogui.screenshot("E:\\Achintya\\Images\\"+name+".png")
        
        else:
            pyautogui.screenshot("E:\\Achintya\\Images\\"+str(datetime.datetime.now()).replace(":","-")+".png")
            
take_screenshot("")