"""
- add typing to class definitions
- generate a list of tasks that I should do today
    x every day tasks
    x tasks that should be done this day of the week
    x tasks that should be done this day of the month
    . tasks that should be done because it's the n-th day
- come up with basic to do data structures
    x recurring task
        x name
        x frequency
            x every day
            x which days of the week
            x every n days
            x which days of the month
- make some example tasks
    x make bed
    x brush teeth
    x apply lotion
    x practice drums
"""
import datetime as dt

import frequencies as f


class Task:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

    def do_on_day(self, day):
        return self.frequency.do_on_day(day)

    def do_today(self):
        return self.frequency.do_today()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Name: {self.name}\nFreq:{self.frequency}"


class MonthlyTask(Task):
    def __init__(self, name, day_number):
        return super().__init__(name, f.MonthlyFrequency(day_number))


class DailyTask(Task):
    def __init__(self, name):
        return super().__init__(name, f.DailyFrequency(1))


class MondayTask(Task):
    def __init__(self, name):
        return super().__init__(name, f.WeeklyFrequency(0))


class TuesdayTask(Task):
    def __init__(self, name):
        return super().__init__(name, f.WeeklyFrequency(1))


class WednesdayTask(Task):
    def __init__(self, name):
        return super().__init__(name, f.WeeklyFrequency(2))


class ThursdayTask(Task):
    def __init__(self, name):
        return super().__init__(name, f.WeeklyFrequency(3))


class FridayTask(Task):
    def __init__(self, name):
        return super().__init__(name, f.WeeklyFrequency(4))


class SaturdayTask(Task):
    def __init__(self, name):
        return super().__init__(name, f.WeeklyFrequency(5))


class SundayTask(Task):
    def __init__(self, name):
        return super().__init__(name, f.WeeklyFrequency(6))


def get_tasks_for_day(task_list, day):
    return list(filter(lambda x: x.do_on_day(day), task_list))


def get_tasks_for_today(task_list):
    today = dt.date.today()
    return get_tasks_for_day(task_list, today)


full_task_list = [
    DailyTask("Make bed"),
    DailyTask("Brush Teeth"),
    DailyTask("Apply Lotion"),
    DailyTask("Go outside"),
    DailyTask("Play Drums"),
    DailyTask("Active Stretching"),
    MondayTask("Push, legs, core workout"),
    WednesdayTask("Move car for street cleaning"),
    MonthlyTask("Stocks", 1),
    MonthlyTask("Stocks", 16),
]
