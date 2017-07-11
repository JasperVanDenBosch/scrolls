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
        rsyslog.configure(config)
        fpath22 = '/etc/rsyslog.d/22-scrolls.conf'
        self.filesys.write.assert_any_call(fpath22,
                                           FWD.replace('0.0.0.0', 'home.com'))
        # written = self.filesys.write.call_args[0][1]
        # self.assertIn('target="home.com"', written)

    def test_configure_restarts_service(self):
        from scrolls.rsyslog import RSyslog
        rsyslog = RSyslog(self.dependencies)
        config = Mock()
        config.server = 'xyz'
        rsyslog.configure(config)
        self.filesys.run.assert_called_with(['service', 'rsyslog', 'restart'])

    def test_configure_nginx(self):
        from scrolls.rsyslog import RSyslog, NGINX
        rsyslog = RSyslog(self.dependencies)
        config = Mock()
        config.server = 'xyz'
        rsyslog.configure(config)
        fpath41 = '/etc/rsyslog.d/41-nginx.conf'
        self.filesys.write.assert_any_call(fpath41,
                                           NGINX.replace('0.0.0.0', 'xyz'))
