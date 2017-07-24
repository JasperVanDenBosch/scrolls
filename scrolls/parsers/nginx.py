

class NginxParser(object):

    def __init__(self, dependencies):
        pass

    def parse(self, string):
        strparts = string.split('"')
        part1, reqpart, statuspart, _, _, uapart, _ = strparts
        reqparts = reqpart.split()
        mdict = {
            'ip': part1.split()[0],
            'httpcode': int(statuspart.split()[0]),
            'httpmethod': reqparts[0],
            'path': reqparts[1],
            'content': reqparts[1],
        }
        return mdict
