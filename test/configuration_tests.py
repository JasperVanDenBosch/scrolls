from test.ditestcase import DITestCase
from mock import Mock, patch
from os.path import expanduser


class ConfigurationTests(DITestCase):

    def setUp(self):
        super(ConfigurationTests, self).setUp()
        self.patchers = {
            'configparser': patch('scrolls.configuration.configparser'),
            'os': patch('scrolls.configuration.os'),
        }
        configparser = self.patchers['configparser'].start()
        self.os = self.patchers['os'].start()
        self.os.path.isfile.return_value = False  # default: no conf file
        self.os.path.expanduser = expanduser
        self.parser = Mock()
        self.parser.sections.return_value = ['scrolls']
        configparser.ConfigParser.return_value = self.parser

    def tearDown(self):
        super(ConfigurationTests, self).tearDown()
        for patcher in self.patchers.values():
            patcher.stop()

    def test_defaults(self):
        from scrolls.configuration import Configuration
        config = Configuration(self.dependencies)
        self.assertEqual(config.server, '0.0.0.0')

    def test_useCommandlineArgs_overrides_defaults_and_config_file(self):
        from scrolls.configuration import Configuration
        config = Configuration(self.dependencies)
        self.assertEqual(config.server, '0.0.0.0')
        self.assertEqual(config.dry_run, False)
        self.parser.get.side_effect = lambda s, k: 'somewhere.else'
        args = Mock()
        args.server = 'remote.com'
        args.dry_run = True
        config.useCommandlineArgs(args)
        self.assertEqual(config.server, 'remote.com')
        self.assertEqual(config.dry_run, True)

    def test_If_config_file_reads_it(self):
        from scrolls.configuration import Configuration
        self.os.path.isfile.return_value = True
        Configuration(self.dependencies)
        self.parser.read.assert_called_with(expanduser('~/scrolls.conf'))

    def test_Uses_values_in_file(self):
        from scrolls.configuration import Configuration
        self.os.path.isfile.return_value = True
        self.parser.getboolean.side_effect = lambda s, k: True
        self.parser.get.side_effect = lambda s, k: 'mothership'
        config = Configuration(self.dependencies)
        self.assertEqual('mothership', config.ticket_secret)

    def test_selectApplications(self):
        from scrolls.configuration import Configuration
        config = Configuration(self.dependencies)
        pkgs = {'nginx': False, 'mongodb': True}
        self.filesys.hasPackage.side_effect = lambda p: pkgs[p]
        apps = config.selectApplications()
        self.assertEqual(apps, {
            'mongodb': '/var/log/mongodb/mongodb.log'
        })
        self.log.selectedApplication.assert_any_call(
            name='mongodb',
            logfile='/var/log/mongodb/mongodb.log'
        )
        pkgs = {'nginx': True, 'mongodb': False}
        self.filesys.hasPackage.side_effect = lambda p: pkgs[p]
        config = Configuration(self.dependencies)
        apps = config.selectApplications()
        self.assertEqual(apps, {
            'nginx-access': '/var/log/nginx/access.log',
            'nginx-error': '/var/log/nginx/error.log',
        })
        self.log.selectedApplication.assert_any_call(
            name='nginx-access',
            logfile='/var/log/nginx/access.log'
        )
        self.log.selectedApplication.assert_any_call(
            name='nginx-error',
            logfile='/var/log/nginx/error.log'
        )
