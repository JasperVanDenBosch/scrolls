from scrolls.models.filter import Filter
from scrolls.idresolver import IdResolver


class Root(object):
    __name__ = ''
    __parent__ = None

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        if key == 'filter':
            return self.getFilter()
        if key == 'id':
            return self.getIdResolver()
        else:
            raise KeyError

    def getFilter(self):
        return Filter(parent=self)

    def getIdResolver(self):
        dependencies = self.request.dependencies
        return IdResolver(parent=self, dependencies=dependencies)
