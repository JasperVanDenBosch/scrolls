import dateutil.parser


class RSyslogParser(object):

    def __init__(self, dependencies):
        self.nginx = dependencies.getNginxParser()

    def parse(self, string):
        parts = string.split()
        content = ' '.join(parts[7:]).strip()
        dt = dateutil.parser.parse(parts[1])
        mdict = {
            'data': string,
            'datetime': dt,
            'hostname': parts[2],
            'app': parts[3],
            'content': content
        }
        if mdict['app'] == 'nginx':
            mdict.update(self.nginx.parse(content))
        return mdict
