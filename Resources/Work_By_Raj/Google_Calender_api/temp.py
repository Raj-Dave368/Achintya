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
# timeMin = is the time. events after this time will be selected in events().list()
eventList = services.events().list(calendarId="primary", timeMin=now).execute()
for i in eventList.get('items'):
    print(i['start'].get('dateTime'))
