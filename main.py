"""
- generate a list of tasks that I should do today
    - every day tasks
    - tasks that should be done this day of the week
    - tasks that should be done because it's the n-th day
- come up with basic to do data structures
    - recurring task
        - name
        - frequency
            - every day
            - which days of the week
            - every n days
- make some example tasks
    - make bed
    - brush teeth
    - apply lotion
    - practice drums
"""
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
