import datetime as dt
import unittest

import frequencies as f
import main as m


class Tests(unittest.TestCase):
    def setUp(self):
        self.today = dt.date.today()
        self.tomorrow = self.today + dt.timedelta(days=1)

    def test_every_other_day_frequency(self):
        freq = f.DailyFrequency(2)

        do_today = freq.do_today()
        do_tomorrow = freq.do_on_day(self.tomorrow)

        self.assertNotEqual(do_today, do_tomorrow)

    def test_every_other_day_task(self):
        freq = f.DailyFrequency(2)
        task = m.Task("Play Drums", freq)

        do_today = task.do_today()
        do_tomorrow = task.do_on_day(self.tomorrow)

        self.assertNotEqual(do_today, do_tomorrow)
