import dateutil.parser


class RSyslogParser(object):

    def __init__(self, dependencies):
        pass

    def parse(self, string):
        parts = string.split()
        content = ' '.join(parts[7:]).strip()
        dt = dateutil.parser.parse(parts[1])
        return {
            'datetime': dt,
            'hostname': parts[2],
            'app': parts[3],
            'content': content
        }
