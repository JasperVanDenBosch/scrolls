from test.ditestcase import DITestCase
from mock import Mock


class RSyslogTests(DITestCase):

    def setUp(self):
        super(RSyslogTests, self).setUp()
        self.filesys.readLines.return_value = []

    def test_configure_forwarding(self):
        from scrolls.rsyslog import RSyslog, FWD
        rsyslog = RSyslog(self.dependencies)
        config = Mock()
        config.server = 'home.com'
        config.selectApplications.return_value = {}
        rsyslog.configure(config)
        fpath22 = '/etc/rsyslog.d/22-scrolls.conf'
        self.filesys.write.assert_any_call(fpath22,
                                           FWD.replace('0.0.0.0', 'home.com'))

    def test_configure_restarts_service(self):
        from scrolls.rsyslog import RSyslog
        rsyslog = RSyslog(self.dependencies)
        config = Mock()
        config.server = 'xyz'
        config.selectApplications.return_value = {}
        rsyslog.configure(config)
        self.filesys.run.assert_called_with(['service', 'rsyslog', 'restart'])

    def test_configure_apps(self):
        from scrolls.rsyslog import RSyslog
        rsyslog = RSyslog(self.dependencies)
        config = Mock()
        config.server = 'xyz'
        config.selectApplications.return_value = {
            'app1': '/p/app1.log',
            'app2': '/p/app2.log',
        }
        rsyslog.configure(config)
        written = self.filesys.write.call_args[0][1]
        fpath = self.filesys.write.call_args[0][0]
        self.assertEqual(fpath, '/etc/rsyslog.d/23-scrolls-apps.conf')
        self.assertIn('module(load="imfile")\n', written)
        self.assertIn('input(type="imfile" File="/p/app1.log" Tag="app1")\n',
                      written)
        self.assertIn('input(type="imfile" File="/p/app2.log" Tag="app2")\n',
                      written)
