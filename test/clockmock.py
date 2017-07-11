

class ClockMock(object):

    def __init__(self):
        self._time = 0

    def advance(self, seconds):
        self._time += seconds

    def time(self):
        return self._time
