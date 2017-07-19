from scrolls.models.counter import Counter


class CounterFactory(object):
    """Builds :class:`Counter` objects"""

    def __init__(self, dependencies):
        pass

    def byHostname(self):
        return Counter('hostname')

    def byApp(self):
        return Counter('app')
