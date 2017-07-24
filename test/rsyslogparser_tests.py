from test.ditestcase import DITestCase
from datetime import datetime
from dateutil.tz import tzoffset


class RSyslogParserTests(DITestCase):

    def test_data_string(self):
        from scrolls.parsers.rsyslog import RSyslogParser
        data = '<54>1 17-01-11T14:44:37.9+01:00 - - - - -  hallo\n'
        mdict = RSyslogParser(self.dependencies).parse(data)
        self.assertIn('data', mdict)
        self.assertEqual(mdict['data'],
                         '<54>1 17-01-11T14:44:37.9+01:00 - - - - -  hallo\n')

    def test_dt_syslog(self):
        from scrolls.parsers.rsyslog import RSyslogParser
        data = '<54>1 2017-01-11T14:44:37.992647+01:00 - - - - -  hallo\n'
        dt = datetime(2017, 1, 11, 14, 44, 37, 992647,
                      tzinfo=tzoffset(None, 3600))
        mdict = RSyslogParser(self.dependencies).parse(data)
        self.assertIn('datetime', mdict)
        self.assertEqual(mdict['datetime'], dt)

    def test_hostname(self):
        from scrolls.parsers.rsyslog import RSyslogParser
        data = ('<38>1 2017-07-18T00:36:21.238521+00:00 www sshd 11943 ' +
                '- - Received disconnect from 59.45.175.67\n')
        mdict = RSyslogParser(self.dependencies).parse(data)
        self.assertIn('hostname', mdict)
        self.assertEqual(mdict['hostname'], 'www')

    def test_app(self):
        from scrolls.parsers.rsyslog import RSyslogParser
        data = ('<38>1 2017-07-18T00:36:21.238521+00:00 www sshd 11943 ' +
                '- - Received disconnect from 59.45.175.67\n')
        mdict = RSyslogParser(self.dependencies).parse(data)
        self.assertIn('app', mdict)
        self.assertEqual(mdict['app'], 'sshd')

    def test_content(self):
        from scrolls.parsers.rsyslog import RSyslogParser
        data = ('<38>1 2017-07-18T00:36:21.238521+00:00 www sshd 11943 ' +
                '- - Received disconnect from 59.45.175.67\n')
        mdict = RSyslogParser(self.dependencies).parse(data)
        self.assertIn('content', mdict)
        self.assertEqual(mdict['content'],
                         'Received disconnect from 59.45.175.67')

    def test_if_nginx_sends_content_through_nginx_parser(self):
        from scrolls.parsers.rsyslog import RSyslogParser
        self.nginxParser.parse.return_value = {'foo': 'bar'}
        data = ('<38>1 2017-07-18T00:36:21.238521+00:00 www nginx 11943 ' +
                '- - I am the nginx message\n')
        mdict = RSyslogParser(self.dependencies).parse(data)
        self.nginxParser.parse.assert_called_with('I am the nginx message')
        self.assertIn('foo', mdict)
        self.assertEqual(mdict['foo'], 'bar')
