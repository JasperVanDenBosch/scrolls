import collections
from operator import itemgetter


class MessageRepository(object):

    def __init__(self, dependencies):
        self.filesys = dependencies.getFilesystem()
        self.message = dependencies.getMessageFactory()
        self.path = 'scrolls.json'

    def serialize(self, message):
        ts = message.getDatetime().timestamp()
        data = message.getData()
        mid = message.getId()
        return (ts, data, mid)

    def add(self, newMessages):
        newRecords = [self.serialize(m) for m in newMessages]
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
            data, mid = record[1:]
            message = self.message.parseFrom(data, withId=mid)
            if filter.accepts(message):
                selectedMessages.append(message)
            if len(selectedMessages) >= n:
                break
        return list(reversed(selectedMessages))

    def getById(self, targetid):
        all = self.filesys.readJson(self.path) or []
        for record in reversed(all):
            data, mid = record[1:]
            message = self.message.parseFrom(data, withId=mid)
            if message.getId() == targetid:
                return message
