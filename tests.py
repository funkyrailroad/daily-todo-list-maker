import datetime as dt
import unittest

import frequencies as f
import main as m


class Tests(unittest.TestCase):
    def setUp(self):
        self.today = dt.date.today()
        self.tomorrow = self.today + dt.timedelta(days=1)
        self.every_other_freq = f.DailyFrequency(2)
        self.every_day_freq = f.DailyFrequency(1)

    def test_every_other_day_frequency(self):
        freq = self.every_other_freq

        do_today = freq.do_today()
        do_tomorrow = freq.do_on_day(self.tomorrow)

        self.assertNotEqual(do_today, do_tomorrow)

    def test_weekday(self):
        wednesday_freq = f.WeeklyFrequency(f.WeeklyFrequency.WEDNESDAY)
        tuesday = dt.date(2022, 10, 4)
        wednesday = dt.date(2022, 10, 5)

        do_tuesday = wednesday_freq.do_on_day(tuesday)
        self.assertFalse(do_tuesday)

        do_wednesday = wednesday_freq.do_on_day(wednesday)
        self.assertTrue(do_wednesday)

    def test_every_other_day_task(self):
        task = m.Task("Play Drums", self.every_other_freq)

        do_today = task.do_today()
        do_tomorrow = task.do_on_day(self.tomorrow)

        self.assertNotEqual(do_today, do_tomorrow)
