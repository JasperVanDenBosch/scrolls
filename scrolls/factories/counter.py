from scrolls.models.counter import Counter


class CounterFactory(object):
    """Builds :class:`Counter` objects"""

    def __init__(self, dependencies):
        pass

    def byHost(self):
        return Counter('host')

    def byApp(self):
        return Counter('app')
