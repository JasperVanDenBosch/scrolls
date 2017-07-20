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
        d = collections.deque(all, 5000)
        d.extend(sortedNewRecords)
        all = list(d)
        all.sort(key=itemgetter(0))
        self.filesys.writeJson(self.path, all)

    def getLatest(self, filter, n=40):
        all = self.filesys.readJson(self.path) or []
        selectedMessages = []
        for record in reversed(all):
            message = self.message.fromTuple(record)
            if filter.accepts(message):
                selectedMessages.append(message)
            if len(selectedMessages) >= n:
                break
        return list(reversed(selectedMessages))
