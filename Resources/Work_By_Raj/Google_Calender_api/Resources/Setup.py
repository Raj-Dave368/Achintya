# maro mahakal


# TODO: evu kaik karvu ke jyare koi navo user Achintya use karva jay to tyare first of all aa 'setup.py' file run thay, because aapde
# TODO: darek user mate different differetn token generate karvana hoy
from googleapiclient import discovery


def setup_calendar_credentials_return_service()->discovery.Resource:
    import os.path

    if os.path.exists('../token.json'):
        os.remove('../token.json')


    from google_auth_oauthlib.flow import InstalledAppFlow
    SCOPE = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file('../credentials.json',scopes=SCOPE)
    creds = flow.run_local_server(port=0)

    with open('../token.json', 'w') as token_file:
        token_file.write(creds.to_json())
        print('Tokens Created and Stored Successfully')

    service = discovery.build('calendar', 'v3', credentials=creds)
    return service
