
'''
- come up with basic to do data structures
    - recurring task
        - name
        - frequency
            - every day
            - which days of the week
            - every n days
- generate a list of tasks that I should do today
    - every day tasks
    - tasks that should be done this day of the week
    - tasks that should be done because it's the n-th day
- make some example tasks
    - make bed
    - brush teeth
    - apply lotion
    - practice drums
'''


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
