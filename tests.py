import datetime as dt
import unittest
from pprint import pprint

import frequencies as f
import main as m


class Tests(unittest.TestCase):
    def setUp(self):
        self.today = dt.date.today()
        self.tomorrow = self.today + dt.timedelta(days=1)
        self.every_other_freq = f.DailyFrequency(2)
        self.every_day_freq = f.DailyFrequency(1)
        self.wednesday_freq = f.WeeklyFrequency(f.WeeklyFrequency.WEDNESDAY)

        self.monday = dt.date(2022, 10, 3)
        self.tuesday = dt.date(2022, 10, 4)
        self.wednesday = dt.date(2022, 10, 5)
        self.thursday = dt.date(2022, 10, 6)
        self.friday = dt.date(2022, 10, 7)
        self.saturday = dt.date(2022, 10, 8)
        self.sunday = dt.date(2022, 10, 9)

    def test_every_day_frequency(self):
        freq = self.every_day_freq

        self.assertTrue(freq.do_today())
        self.assertTrue(freq.do_on_day(self.tomorrow))
        self.assertTrue(freq.do_on_day(self.monday))
        self.assertTrue(freq.do_on_day(self.tuesday))
        self.assertTrue(freq.do_on_day(self.wednesday))
        self.assertTrue(freq.do_on_day(self.thursday))
        self.assertTrue(freq.do_on_day(self.friday))
        self.assertTrue(freq.do_on_day(self.saturday))
        self.assertTrue(freq.do_on_day(self.sunday))

    def test_every_other_day_frequency(self):
        freq = self.every_other_freq

        do_today = freq.do_today()
        do_tomorrow = freq.do_on_day(self.tomorrow)

        self.assertNotEqual(do_today, do_tomorrow)

    def test_weekly_frequency_class_variables(self):
        self.assertEqual(self.monday.weekday(), f.WeeklyFrequency.MONDAY)
        self.assertEqual(self.tuesday.weekday(), f.WeeklyFrequency.TUESDAY)
        self.assertEqual(self.wednesday.weekday(), f.WeeklyFrequency.WEDNESDAY)
        self.assertEqual(self.thursday.weekday(), f.WeeklyFrequency.THURSDAY)
        self.assertEqual(self.friday.weekday(), f.WeeklyFrequency.FRIDAY)
        self.assertEqual(self.saturday.weekday(), f.WeeklyFrequency.SATURDAY)
        self.assertEqual(self.sunday.weekday(), f.WeeklyFrequency.SUNDAY)

    def test_monthly_task(self):
        day_number = 4
        task = m.MonthlyTask("Monthly task", day_number)
        for i in range(1, 31):
            day = dt.date(2022, 11, i)
            do_on_day = task.do_on_day(day)
            if i == day_number:
                self.assertTrue(do_on_day)
                continue
            self.assertFalse(do_on_day)
        pass

    def test_weekday(self):
        do_tuesday = self.wednesday_freq.do_on_day(self.tuesday)
        self.assertFalse(do_tuesday)

        do_wednesday = self.wednesday_freq.do_on_day(self.wednesday)
        self.assertTrue(do_wednesday)

    def test_every_other_day_task(self):
        task = m.Task("Play Drums", self.every_other_freq)

        do_today = task.do_today()
        do_tomorrow = task.do_on_day(self.tomorrow)

        self.assertNotEqual(do_today, do_tomorrow)

    def test_daily_task(self):
        task = m.DailyTask("Get outside")
        self.assertTrue(task.do_today())

    def test_monday_task(self):
        task = m.MondayTask("Push, legs, core workout")
        self.assertTrue(task.do_on_day(self.monday))
        self.assertFalse(task.do_on_day(self.tuesday))

    def test_tuesday_task(self):
        task = m.TuesdayTask("Functional, pull, forearm workout")
        self.assertFalse(task.do_on_day(self.monday))
        self.assertTrue(task.do_on_day(self.tuesday))

    def test_1(self):
        full_task_list = [
            m.DailyTask("Brush Teeth"),
            m.DailyTask("Apply Lotion"),
            m.DailyTask("Go outside"),
            m.DailyTask("Play Drums"),
            m.DailyTask("Active Stretching"),
            m.WednesdayTask("Move car for street cleaning"),
        ]

        tuesday_task_list = m.get_tasks_for_day(full_task_list, self.today)

        wednesday_task_list = m.get_tasks_for_day(full_task_list,
                                                  self.wednesday)

        self.assertLess(len(tuesday_task_list), len(wednesday_task_list))
