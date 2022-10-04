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

    def do_on_day(self, day):
        """Determine if the activity should be done on a given day."""
        start = get_days_since_epoch()
        days_elapsed = (day - start).days
        return  days_elapsed % self.n

    def do_today(self):
        """Determine if the activity should be done today."""
        return self.do_on_day(dt.date.today())



def get_days_since_epoch():
    return dt.datetime.utcfromtimestamp(0).date()


