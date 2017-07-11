from test.ditestcase import DITestCase
from mock import patch, Mock


class ConfigurationTests(DITestCase):

    def setUp(self):
        super(ConfigurationTests, self).setUp()
        self.patchers = {
            'argparse': patch('scrolls.entrypoint.argparse'),
            'dependencies': patch('scrolls.entrypoint.scrolls.dependencies')
        }
        argparse = self.patchers['argparse'].start()
        self.args = Mock()
        argparse.ArgumentParser().parse_args.return_value = self.args
        dependencies = self.patchers['dependencies'].start()
        dependencies.Dependencies.return_value = self.dependencies

    def tearDown(self):
        super(ConfigurationTests, self).tearDown()
        for patcher in self.patchers.values():
            patcher.stop()

    def test_configure(self):
        from scrolls.entrypoint import main
        self.args.command = 'configure'
        main()
        self.config.useCommandlineArgs.assert_called_with(self.args)
        self.rsyslog.configure.assert_called_with(self.config)
