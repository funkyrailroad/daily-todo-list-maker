from abc import ABC, abstractmethod
import datetime as dt


class Frequency(ABC):

    @abstractmethod
    def do_today(today):
        """Determine if the activity should be done today"""
        pass


class WeeklyFrequency:
    def __init__(self, day):
        pass


class DailyFrequency:
    def __init__(self, n):
        self.n = n

    def do_today(self, today):
        """Determine if the activity should be done today"""
        start = get_days_since_epoch()
        days_elapsed = (today - start).days
        return  days_elapsed % self.n


def get_days_since_epoch():
    return dt.datetime.utcfromtimestamp(0).date()


