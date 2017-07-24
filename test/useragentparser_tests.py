from test.ditestcase import DITestCase

UA = ('Mozilla/5.0 (X11; Linux x86_64)' +
      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115' +
      ' Safari/537.36')


class UseragentParserTests(DITestCase):

    def test_nginx(self):
        from scrolls.parsers.useragent import UseragentParser
        mdict = UseragentParser(self.dependencies).parse(UA)
        self.assertEqual(mdict['browser-family'], 'Chrome')
