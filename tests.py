import datetime as dt
import unittest

import frequencies as f


class Tests(unittest.TestCase):
    def test_every_other_day(self):
        # start with a test for a frequency that happens every other day.
        freq = f.DailyFrequency(2)

        # define a date
        today = dt.date.today()

        # see if it should be done on that day
        do_today = freq.do_today()

        # add a day to the date
        tomorrow = today + dt.timedelta(days=1)

        # see if it should be done on that day
        do_tomorrow = freq.do_on_day(tomorrow)

        # it should not be done on two consecutive days
        self.assertNotEqual(do_today, do_tomorrow)
