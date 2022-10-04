import datetime as dt
from abc import ABC, abstractmethod


class Frequency(ABC):
    @abstractmethod
    def do_today(today):
        """Determine if the activity should be done today"""
        pass

    @abstractmethod
    def do_on_day(day):
        pass


class WeeklyFrequency:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    def __init__(self, day):
        self.day = day
        pass

    def do_on_day(self, day):
        return day.weekday() == self.day

    def do_today(self):
        return self.do_on_day(dt.date.today())


class DailyFrequency:
    def __init__(self, n):
        self.n = n

    def do_on_day(self, day):
        """Determine if the activity should be done on a given day."""
        start = get_days_since_epoch()
        days_elapsed = (day - start).days
        return not (days_elapsed % self.n)

    def do_today(self):
        """Determine if the activity should be done today."""
        return self.do_on_day(dt.date.today())


def get_days_since_epoch():
    return dt.datetime.utcfromtimestamp(0).date()
