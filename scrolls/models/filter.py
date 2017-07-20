

class Filter(object):

    KEYS = ('app', 'hostname')

    def __init__(self, parent, segment=None):
        self.resolvable = False
        self.isKey = False
        if segment:
            if segment in self.KEYS:
                self.isKey = True
            else:
                self.resolvable = True
        self.__name__ = segment or 'filter'
        self.__parent__ = parent
        self.path = parent.path + (segment,) if segment else ()

    def __getitem__(self, key):
        if self.isKey or key in self.KEYS:
            return Filter(parent=self, segment=key)
        else:
            raise KeyError

    def getFilter(self):
        return self

    def accepts(self, message):
        if len(self.path) < 2:
            return True
        mdict = message.toDict()
        if self.path[1] == mdict.get(self.path[0]):
            return True
        return False
