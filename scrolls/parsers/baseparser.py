

class BaseParser(object):

    def parse(self, string):
        try:
            return self._parse(string)
        except Exception as exc:
            return {'scrolls.parse-exception': str(exc)}
