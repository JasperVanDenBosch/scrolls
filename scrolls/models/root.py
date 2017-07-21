from scrolls.models.filter import Filter


class Root(object):
    __name__ = ''
    __parent__ = None

    def __init__(self, request):
        pass

    def __getitem__(self, key):
        if key == 'filter':
            return Filter(parent=self)
        else:
            raise KeyError

    def getFilter(self):
        return self['filter']
