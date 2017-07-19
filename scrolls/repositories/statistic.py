

class StatisticRepository(object):

    def __init__(self, dependencies):
        self.filesys = dependencies.getFilesystem()

    def update(self, name, newCounts):
        path = name + '.json'
        counts = self.filesys.readJson(path) or {}
        for key, newCount in newCounts.items():
            jsonKey = ','.join(key)
            if jsonKey in counts:
                counts[jsonKey] += newCount
            else:
                counts[jsonKey] = newCount
        self.filesys.writeJson(path, counts)

    def get(self, name):
        path = name + '.json'
        record = self.filesys.readJson(path) or {}
        return {tuple(k.split(',')): v for k, v in record.items()}
