import dateutil.parser


class Message(object):

    def __init__(self, client, data, shortuuid):
        self.client = client
        self.data = data
        self.shortuuid = shortuuid

    def getApp(self):
        return self.data.split()[3]

    def getContent(self):
        return ' '.join(self.data.split()[7:]).strip()

    def getDatetime(self):
        s = self.data.split()[1]
        return dateutil.parser.parse(s)

    def getHostname(self):
        return self.data.split()[2]

    def getId(self):
        dt = self.getDatetime()
        return dt.strftime('%Y%m%d%H%M%S%f')[:-3] + self.shortuuid

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
        return self.getTimestamp(), self.client, self.data, self.shortuuid

    def resourcify(self, parent):
        self.__parent__ = parent
        self.__name__ = self.getId()
