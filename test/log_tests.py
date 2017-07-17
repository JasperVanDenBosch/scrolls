from test.ditestcase import DITestCase
from mock import patch


class LogTests(DITestCase):

    def setUp(self):
        super(LogTests, self).setUp()
        self.patchers = {
            'print': patch('scrolls.log.print'),
        }
        self.print = self.patchers['print'].start()

    def tearDown(self):
        super(LogTests, self).tearDown()
        for patcher in self.patchers.values():
            patcher.stop()

    def test_foundPackage(self):
        from scrolls.log import Log
        log = Log(self.dependencies)
        log.foundPackage('abc')
        self.print.assert_called_with('[scrolls] Found system package "abc".')

    def test_ranCommand(self):
        from scrolls.log import Log
        log = Log(self.dependencies)
        log.ranCommand(['a', 'b', 'c'], True)
        msg = '[scrolls] (dry run) Would have ran command "a b c".'
        self.print.assert_called_with(msg)
        log.ranCommand(['a', 'b', 'c'], False)
        msg = '[scrolls] Ran command "a b c".'
        self.print.assert_called_with(msg)

    def test_selectedApplication(self):
        from scrolls.log import Log
        log = Log(self.dependencies)
        log.selectedApplication(name='abc', logfile='/p/abc.log')
        msg = '[scrolls] Selected application "abc" with logfile "/p/abc.log".'
        self.print.assert_called_with(msg)

    def test_wroteFile(self):
        from scrolls.log import Log
        log = Log(self.dependencies)
        log.wroteFile('/p/f.x', '1234567890', True)
        m = '[scrolls] (dry run) Would have written 10 characters to "/p/f.x".'
        self.print.assert_called_with(m)
        log.wroteFile('/p/f.x', '1234567890', False)
        m = '[scrolls] Wrote 10 characters to file "/p/f.x".'
        self.print.assert_called_with(m)
