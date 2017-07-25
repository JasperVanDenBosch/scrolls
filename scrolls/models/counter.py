

class Counter(object):

    def __init__(self, name, dtBinFormat=None):
        self.name = name
        self.dtBinFormat = dtBinFormat
        self.counts = {}

    def add(self, message):
        if self.dtBinFormat:
            dt = message.toDict().get('datetime')
            val = dt.strftime(self.dtBinFormat)
        else:
            val = message.toDict().get(self.name)
        key = (self.name, val)
        if key in self.counts:
            self.counts[key] += 1
        else:
            self.counts[key] = 1

    def reset(self):
        self.counts = {}
