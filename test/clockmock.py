from datetime import datetime


class ClockMock(object):

    def __init__(self):
        self._time = 0
        self.cachedNow = datetime.now()

    def now(self):
        return self.cachedNow

    def advance(self, seconds):
        self._time += seconds

    def time(self):
        return self._time
