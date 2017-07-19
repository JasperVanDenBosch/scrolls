import collections
from operator import itemgetter


class MessageRepository(object):

    def __init__(self, dependencies):
        self.filesys = dependencies.getFilesystem()
        self.message = dependencies.getMessageFactory()
        self.path = 'scrolls.json'

    def add(self, newMessages):
        newRecords = [m.toTuple() for m in newMessages]
        sortedNewRecords = sorted(newRecords, key=itemgetter(0))
        all = self.filesys.readJson(self.path) or []
        d = collections.deque(all, 1000)
        d.extend(sortedNewRecords)
        all = list(d)
        all.sort(key=itemgetter(0))
        self.filesys.writeJson(self.path, all)

    def getLatest(self, n=10):
        all = self.filesys.readJson(self.path) or []
        latestRecords = all[-n:]
        return [self.message.fromTuple(t) for t in latestRecords]
