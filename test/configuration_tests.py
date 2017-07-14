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
        self.parser.get.side_effect = lambda s, k: 'somewhere.else'
        args = Mock()
        args.server = 'remote.com'
        config.useCommandlineArgs(args)
        self.assertEqual(config.server, 'remote.com')

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
