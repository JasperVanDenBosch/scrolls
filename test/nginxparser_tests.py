from test.ditestcase import DITestCase

NGMSG = ('127.0.0.1 - - [22/Jul/2017:16:44:46 +0100] "GET /bla' +
         ' HTTP/1.1" 404 209 "-" "UAString"\n')


class NginxParserTests(DITestCase):

    def test_nginx(self):
        from scrolls.parsers.nginx import NginxParser
        mdict = NginxParser(self.dependencies).parse(NGMSG)
        self.assertEqual(mdict['httpcode'], 404)
        self.assertEqual(mdict['httpmethod'], 'GET')
        self.assertEqual(mdict['path'], '/bla')
        self.assertEqual(mdict['ip'], '127.0.0.1')
        self.assertEqual(mdict['content'], '/bla')
