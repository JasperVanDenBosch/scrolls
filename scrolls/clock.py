import time as stdlib_time
import datetime as stdlib_datetime


class Clock(object):

    def time(self):
        return stdlib_time.time()

    def now(self):
        return stdlib_datetime.datetime.now()
