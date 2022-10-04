import datetime as dt
from abc import ABC, abstractmethod


class Frequency(ABC):
    @abstractmethod
    def do_on_day(day):
        pass

    def do_today(self):
        return self.do_on_day(dt.date.today())


class MonthlyFrequency(Frequency):
    def __init__(self, day_of_the_month):
        self.day = day_of_the_month

    def do_on_day(self, day):
        return day.day == self.day


class WeeklyFrequency(Frequency):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    def __init__(self, day):
        self.day = day

    def do_on_day(self, day):
        return day.weekday() == self.day


class DailyFrequency(Frequency):
    def __init__(self, n):
        self.n = n

    def do_on_day(self, day):
        """Determine if the activity should be done on a given day."""
        start = get_days_since_epoch()
        days_elapsed = (day - start).days
        return not (days_elapsed % self.n)


def get_days_since_epoch():
    return dt.datetime.utcfromtimestamp(0).date()
