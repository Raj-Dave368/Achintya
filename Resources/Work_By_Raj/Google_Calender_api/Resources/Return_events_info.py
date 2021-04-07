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


def return_events_info(cmd: str, service):

    """
    command should be one of below:
    how many events do i have "Today"
    how many events do i have "Tomorrow"
    how many events do i have "on" "21" "April" (here twenty first na bolvu: twenty one bolvu [command ma])
    """
    cmd = cmd.lower()

    # -------- parsing command
    import datetime
    import pytz
    date_of_event = None
    if "today" in cmd:
        date_of_event = datetime.datetime.utcnow()
    elif "tomorrow" in cmd:
        today = datetime.datetime.today()
        str_date = str(today.day)
        if len(str_date) == 1:
            # we want date to have of two digit i.e. if date is 1 then we want 01 i.e. added 0 at the beginning
            # if date is 11 then we want 11 i.e. no change here
            str_date = '0' + str_date
        str_month = str(today.month)
        if len(str_month) == 1:
            str_month = '0' + str_month
        str_year = today.year
        date_of_event = datetime.datetime.strptime(f"{str_date}-{str_month}-{str_year}T00:00:00",
                                                   "%d-%m-%YT%H:%M:%S") + datetime.timedelta(days=1)
    elif "on" in cmd:
        list_ = cmd.split()
        str_date = list_[-2]

        if len(str_date) == 1:
            # we want date to have of two digit i.e. if date is 1 then we want 01 i.e. added 0 at the beginning
            # if date is 11 then we want 11 i.e. no change here
            str_date = '0' + str_date
        str_month = list_[-1]
        str_year = str(datetime.datetime.today().year)

        date_of_event = datetime.datetime.strptime(f"{str_date}-{str_month}-{str_year}T00:00:00+05:30",
                                                   "%d-%B-%YT%H:%M:%S+05:30")



    if date_of_event:
        calenderList = service.events().list(calendarId='primary',
                                             timeMin=date_of_event.astimezone(pytz.timezone('Asia/kolkata')).isoformat(),
                                             timeMax=(date_of_event +
                                                      datetime.timedelta(hours=23,)).astimezone(pytz.timezone('Asia/kolkata')).isoformat(),
                                             maxResults=7,
                                             singleEvents=True,
                                             orderBy='startTime'
                                             ).execute()

        print(date_of_event)
        print(date_of_event + datetime.timedelta(days=1))
        event_list = calenderList['items']

        print(event_list)
        # list of filtered events
        # filtered_events = [ [ [hour, minutes, AM_PM], title, duration] ]
        filtered_events = []
        for i in event_list:
            # title
            title = i['summary']
            # start_date
            startFormattedDateTime = str(i['start']['dateTime'])
            startFormattedDateTime = startFormattedDateTime[0:startFormattedDateTime.rfind('+')]
            startDateTime = datetime.datetime.strptime(startFormattedDateTime, "%Y-%m-%dT%H:%M:%S")
            # endDateTime
            endFormattedDateTime = str(i['end']['dateTime'])
            endFormattedDateTime = endFormattedDateTime[0:endFormattedDateTime.rfind('+')]
            endDateTime = datetime.datetime.strptime(endFormattedDateTime, "%Y-%m-%dT%H:%M:%S")
            # how long event is
            total_seconds = (endDateTime - startDateTime).seconds
            duration_hour = 0
            duration_minutes = 0
            if total_seconds >= 3600:
                duration_hour = (endDateTime - startDateTime).seconds // 3600
            duration_minutes = (((endDateTime - startDateTime).seconds - (duration_hour*3600)) % 3600) // 60
            duration = [duration_hour, duration_minutes]
            # -------- getting hour, minutes, seconds etc
            minutes = startDateTime.minute

            if startDateTime.hour > 12:
                hour = startDateTime.hour - 12
                AM_PM = 'p m '
            elif startDateTime.hour == 12 and startDateTime.minute > 0:
                hour = startDateTime.hour
                AM_PM = 'p m '
            else:
                hour = startDateTime.hour
                AM_PM = 'a m '

            filtered_events.append([title, [hour, minutes, AM_PM], duration])

        for each_event in filtered_events:
            print(each_event)
        return filtered_events,cmd
#


filtered_events, cmd = return_events_info("how many events do I have tomorrow", service=service)


import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 186)


if 'have on ' in cmd:
    what_date_user_asked = cmd[cmd.find('have on ')+4+4:]
elif 'had on ' in cmd:
    what_date_user_asked = cmd[cmd.find('had on ')+3+4:]
elif 'have ' in cmd:
    what_date_user_asked = cmd[cmd.find('have ')+4+1:]
else:
    what_date_user_asked = cmd[cmd.find('had ')+3+1:]


if len(filtered_events) == 0:
    print(f"you don't have any events for {what_date_user_asked}")
    engine.say(f"you don't have any events for {what_date_user_asked}")
    engine.runAndWait()
elif len(filtered_events) <= 7:
    print(f"you have {len(filtered_events)} events for {what_date_user_asked}!")
    engine.say(f"you have {len(filtered_events)} events for {what_date_user_asked} !")
    engine.runAndWait()
else:
    print(f"you have so many events for {what_date_user_asked} as displayed")
    engine.say(f"you have so many events for {what_date_user_asked} as displayed")
    engine.runAndWait()

if len(filtered_events) <= 7:
    for number, each in zip(range(1, len(filtered_events)+1), filtered_events):
        achintya_speakable_format = str(number) + "! " + each[0] + ", at, " + str(each[1][0]) + " "
        if str(each[1][1]) != '0':
            achintya_speakable_format += str(each[1][1])
        achintya_speakable_format += " " + str(each[1][2]) + '!'
        if each[-1][0] > 0:
            achintya_speakable_format += f"Which is {each[-1][0]} hours"
            if each[-1][1] > 0:
                achintya_speakable_format += f"and {each[-1][1]} minutes long"
            else:
                achintya_speakable_format += "long"
        else:
            achintya_speakable_format += f"Which is {each[-1][1]} minutes long"
        engine.say(achintya_speakable_format)
        engine.runAndWait()
        from time import sleep
        sleep(1)
#
