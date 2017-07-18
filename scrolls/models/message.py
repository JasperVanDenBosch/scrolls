import dateutil.parser
import time


class Message(object):

    def __init__(self, client, data):
        self.client = client
        self.data = data

    def getDatetime(self):
        s = self.data.split()[1]
        return dateutil.parser.parse(s)

    def getTimestamp(self):
        return self.getDatetime().timestamp()

    def toTuple(self):
        return self.getTimestamp(), self.client, self.data
