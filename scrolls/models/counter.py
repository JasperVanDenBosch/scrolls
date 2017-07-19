

class Counter(object):

    def __init__(self, attribute):
        self.name = attribute
        self.counts = {}

    def add(self, message):
        val = message.toDict().get(self.name)
        key = (self.name, val)
        if key in self.counts:
            self.counts[key] += 1
        else:
            self.counts[key] = 1

    def reset(self):
        self.counts = {}
