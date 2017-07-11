import collections
import dateutil.parser


class MessageRepository(object):

    def __init__(self, dependencies):
        self.filesys = dependencies.getFilesystem()
        self.path = 'scrolls.json'

    def add(self, newMessages):
        def sortkey(m):
            s = m[1].split()[1]
            return dateutil.parser.parse(s)
        if not newMessages:
            return
        newRecords = [self.messageToRecord(m) for m in newMessages]
        sortedNewRecords = sorted(newRecords, key=sortkey)
        all = self.filesys.readJson(self.path) or []
        d = collections.deque(all, 1000)
        d.extend(sortedNewRecords)
        all = list(d)
        all.sort(key=sortkey)
        self.filesys.writeJson(self.path, all)

    def getLatest(self, n=10):
        all = self.filesys.readJson(self.path) or []
        return all[-n:]

    def messageToRecord(self, message):
        return message
