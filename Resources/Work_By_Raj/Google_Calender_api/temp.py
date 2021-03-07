# jay Dada


import os.path

creds = None

SCOPE = ["https://www.googleapis.com/auth/calendar"]
path = "Achintya\\Resources\\Work_By_Raj\\Google_Calender_api\\"
path = ""

if os.path.exists(path + "token.json"):
    from google.oauth2.credentials import Credentials

    creds = Credentials.from_authorized_user_file(path + "token.json", SCOPE)
    print("Credentials Successfully Loaded to token.json")

print(creds.valid)
# if not creds or not creds.valid:
#     print("creds is not valid")
#     print("Just wait ...")
#     if creds and creds.expired and creds.refresh_token:
#         print("creds is expired just wait ...")
#         print("we are trying to refresh it wait ...")
#         from google.auth.transport.requests import Request
#         creds.refresh(Request())
#     else:
#         print("invalid data, need to verify your account again ...")
#         from google_auth_oauthlib.flow import InstalledAppFlow
#         flow = InstalledAppFlow.from_client_secrets_file(path+"credentials.json", SCOPE)
#         creds = flow.run_local_server(port=0)
#
#     with open(path + "token.json", 'w') as token:
#         token.write(creds.to_json())
#         print("New Token is Generated and Stored Successfully")


from googleapiclient.discovery import build

services = build('calendar', 'v3', credentials=creds)

import datetime
now = datetime.datetime.utcnow().isoformat() + 'Z'
print(now)
# timeMin = is the time. events after this time will be selected in events().list()
# print(dir(services.events()))
# eventList = services.events().list(calendarId="primary", timeMin=now).execute()
# for i in eventList.get('items'):
#     print(i['start'].get('dateTime'))

import pytz

print(services.events().insert(calendarId='primary',body=
    {
        'summary' : 'Demo From Python',
        #  way 1
        # 'start': {'dateTime': datetime.datetime.utcnow().isoformat() + 'Z'},
        # 'end': {'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(hours=5)).isoformat() + 'Z'}
        # 'Z' - It is indicating UTC timeZone if you want your own local timezone then give end.timeZone but now you
        # should remove + 'Z' otherwise it will produce an error

        # way 2
        # 'start': {'dateTime':(datetime.datetime(2021,3,8,3,00,00,00,)).isoformat(),'timeZone':"Asia/Kolkata"},
        # 'end': {'dateTime': (datetime.datetime(2021,3,8,5,00,00,00,)).isoformat(),'timeZone':"Asia/Kolkata"},

        # way 3
        'start': {'dateTime': (datetime.datetime(2021, 3, 8, 13, 00, 00, 00).astimezone(tz=pytz.utc)).isoformat()},
        'end': {'dateTime': (datetime.datetime(2021, 3, 8, 15, 00, 00, 00).astimezone(tz=pytz.utc)).isoformat()},
    },

).execute())