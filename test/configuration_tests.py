from test.ditestcase import DITestCase
from mock import Mock


class ConfigurationTests(DITestCase):

    def test_defaults(self):
        from scrolls.configuration import Configuration
        config = Configuration(self.dependencies)
        self.assertEqual(config.server, '0.0.0.0')

    def test_useCommandlineArgs_overrides_defaults(self):
        from scrolls.configuration import Configuration
        config = Configuration(self.dependencies)
        self.assertEqual(config.server, '0.0.0.0')
        args = Mock()
        args.server = 'remote.com'
        config.useCommandlineArgs(args)
        self.assertEqual(config.server, 'remote.com')
