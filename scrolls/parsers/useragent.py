from ua_parser import user_agent_parser
from scrolls.parsers.baseparser import BaseParser


class UseragentParser(BaseParser):

    def __init__(self, dependencies):
        pass

    def _parse(self, string):
        uadict = user_agent_parser.Parse(string)
        mdict = {}
        if 'user_agent' in uadict:
            if 'family' in uadict['user_agent']:
                mdict['browser-family'] = uadict['user_agent']['family']
        return mdict
