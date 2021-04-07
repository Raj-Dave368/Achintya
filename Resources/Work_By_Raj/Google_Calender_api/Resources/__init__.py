# jay mahakal


import Setup
import Return_events_info


# below function [Setup.setup_calendar_credentials_return_service()]  should run only once
service = Setup.setup_calendar_credentials_return_service()
print(Return_events_info.return_events_info("Give details about calendar events for today", service=service))
