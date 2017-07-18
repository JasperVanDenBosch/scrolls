import dateutil.parser


class Message(object):

    def __init__(self, client, data):
        self.client = client
        self.data = data

    def getApp(self):
        return self.data.split()[3]

    def getContent(self):
        return ' '.join(self.data.split()[7:]).strip()

    def getDatetime(self):
        s = self.data.split()[1]
        return dateutil.parser.parse(s)

    def getHostname(self):
        return self.data.split()[2]

    def getTimestamp(self):
        return self.getDatetime().timestamp()

    def toDict(self):
        return {
            'datetime': self.getDatetime(),
            'hostname': self.getHostname(),
            'app': self.getApp(),
            'content': self.getContent(),
        }

    def toTuple(self):
        return self.getTimestamp(), self.client, self.data
