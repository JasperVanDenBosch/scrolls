from test.ditestcase import DITestCase
from mock import patch

UA = ('Mozilla/5.0 (X11; Linux x86_64)' +
      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115' +
      ' Safari/537.36')


class UseragentParserTests(DITestCase):

    def test_browser_family(self):
        from scrolls.parsers.useragent import UseragentParser
        mdict = UseragentParser(self.dependencies).parse(UA)
        self.assertEqual(mdict['browser-family'], 'Chrome')

    def test_if_exception_during_parsing_saves_it_and_sets_basics(self):
        from scrolls.parsers.useragent import UseragentParser
        with patch('scrolls.parsers.useragent.user_agent_parser') as ualib:
            ualib.Parse.side_effect = ValueError('Pfff!')
            mdict = UseragentParser(self.dependencies).parse(UA)
            self.assertIn('scrolls.parse-exception', mdict)
            self.assertEqual('Pfff!', mdict['scrolls.parse-exception'])
