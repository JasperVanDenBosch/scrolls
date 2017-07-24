

class Message(object):

    def __init__(self, mdict):
        self.mdict = mdict

    def getDatetime(self):
        return self.mdict['datetime']

    def getId(self):
        return self.mdict['id']

    def getData(self):
        return self.mdict['data']

    def toDict(self):
        return self.mdict

    def resourcify(self, parent):
        self.__parent__ = parent
        self.__name__ = self.getId()
