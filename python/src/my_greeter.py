from datetime import datetime
from enum import Enum


class GREETING_TIMESLOT(Enum):
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3


class MyGreeter:

    def __init__(self):
        pass

    def get_timeslot(self, hour):
        # Based on the hour value, return corresponding greeting timeslot
        if 6 <= hour < 12:
            return GREETING_TIMESLOT.MORNING
        elif 12 <= hour < 18:
            return GREETING_TIMESLOT.AFTERNOON
        else:
            return GREETING_TIMESLOT.EVENING

    def greeting_timeslot(self, greeting_timeslot):
        if greeting_timeslot == GREETING_TIMESLOT.MORNING:
            return self.greeting_morning()
        elif greeting_timeslot == GREETING_TIMESLOT.AFTERNOON:
            return self.greeting_afternoon()
        else:
            return self.greeting_evening()

    # greeting behavior function for morning
    def greeting_morning(self):
        return "Good morning"

    # greeting behavior function for afternoon
    def greeting_afternoon(self):
        return "Good afternoon"

    # greeting behavior function for evening
    def greeting_evening(self):
        return "Good evening"

    def greeting(self, current_time=None):
        """
        Returns a greeting message based on the current time.
        If no current_time is provided, it uses the current time on the system.

        Param current_time:
            Optional, datetime object of the current time.
        Return:
            A greeting message based on the hour of time.
        """

        # If current_time is not provided, use the current system time
        if current_time is None:
            current_time = datetime.now()

        # Extract the hour of the current time
        hour = current_time.hour
        time_slot = self.get_timeslot(hour)

        return self.greeting_timeslot(time_slot)
