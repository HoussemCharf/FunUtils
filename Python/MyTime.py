"""
This module will help you to work with time object.
"""


class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        if self.hours > time2.hours:
            return True
        if self.hours < time2.hours:
            return False

        if self.minutes > time2.minutes:
            return True
        if self.minutes < time2.minutes:
            return False
        if self.seconds > time2.seconds:
            return True

        return False

    def between(self, time1, time2):
        return True if time1 < self and self < time2 else False

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        return str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + ":" + str(self.seconds).zfill(2)

    def __gt__(self, t):
        t1 = self.to_seconds()
        t2 = t.to_seconds()
        return True if t1 > t2 else False

    def __lt__(self, t):
        t1 = self.to_seconds()
        t2 = t.to_seconds()
        return True if t1 < t2 else False


def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)
