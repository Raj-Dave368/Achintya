# maro mahakal


from googleapiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials


import os.path
# step0: we need to tell the API that how much access on calendar we want so we need to
# define a variable SCOPE and need to pass it wherever required
SCOPE = ['https://www.googleapis.com/auth/calendar']

# step1: initialize creds from Credentials.from_authorized_user_file(../token.json)
creds = None

if os.path.exists('../token.json'):
    creds = Credentials.from_authorized_user_file('../token.json')
else:
    from Resources.Work_By_Raj.Google_Calender_api.Resources import Setup
    Setup.setup_calendar_credentials()

# step2: initialize service from discovery.build
service = discovery.build('calendar', 'v3', credentials=creds)

print(dir(service))
if service:
    print("SetUp SuccessFull")



import datetime
calenderList = service.events().list(calendarId='primary',
                                     timeMin=(datetime.datetime.utcnow()).isoformat() + 'Z',
                                     maxResults=10,
                                     singleEvents=True,
                                     orderBy='startTime'
                                     ).execute()
event_list = calenderList['items']

# list of filtered events
# filtered_events = [ [ [hour, minutes, AM_PM], title] ]
filtered_events = []
for i in event_list:
    title = i['summary']
    formattedDateTime = str(i['start']['dateTime'])
    formattedDateTime = formattedDateTime[0:formattedDateTime.rfind('+')]
    dateTime = datetime.datetime.strptime(formattedDateTime, "%Y-%m-%dT%H:%M:%S")

    now = datetime.datetime.now()
    if dateTime.date() == now.date():
        hour = None
        minutes = dateTime.minute
        AM_PM = "p.m."

        if dateTime.hour > 12:
            hour = dateTime.hour - 12
            AM_PM = 'p.m.'
        elif dateTime.hour == 12 and dateTime.minute > 0:
            hour = dateTime.hour
            AM_PM = 'p.m.'
        else:
            hour = dateTime.hour
            AM_PM = 'a.m.'

        filtered_events.append([[hour, minutes, AM_PM], title])


print(filtered_events)

import pyttsx3
import win10toast

engine = pyttsx3.init()
engine.setProperty('rate', 186)

collection_of_events_to_notify = ""
for each in filtered_events:
    collection_of_events_to_notify = collection_of_events_to_notify + "\n" + each[1] + " " + "@ " + str(each[0][0]) + ":" + \
                                     str(each[0][1]) + " " + str(each[0][2]).upper()


if len(filtered_events) == 0:
    print("you don't have any events")
    engine.say("you don't have any events")
    engine.runAndWait()
elif len(filtered_events) <= 5:
    print("you have " + str(len(filtered_events)) + " events Today!")
    engine.say("you have " + str(len(filtered_events)) + " events Today!")
    engine.runAndWait()
else:
    print("you have many events today as displayed")
    engine.say("you have many events today as displayed")
    engine.runAndWait()

    # import ctypes  # An included library with Python install.
    # ctypes.windll.user32.MessageBoxW(0, collection_of_events_to_notify, "Events", 0)
    # import easygui
    # easygui.msgbox(collection_of_events_to_notify, title="Events")
    import pymsgbox
    pymsgbox.alert(collection_of_events_to_notify, "Events")
    # response = pymsgbox.prompt('What is your name?')

from plyer import notification

notification.notify(title="Events",
                    message=collection_of_events_to_notify,
                    app_icon='event.ico',
                    toast=True,
                    timeout=30
                    )

if len(filtered_events) <= 5:
    for number, each in zip(range(1, len(filtered_events)+1), filtered_events):
        achintya_speakable_format = str(number) + ". " + each[1] + ", at, " + str(each[0][0]) + " " +\
                                    str(each[0][1]) + " " + str(each[0][2])
        engine.say(achintya_speakable_format)
        engine.runAndWait()

