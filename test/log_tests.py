from test.ditestcase import DITestCase


class LogTests(DITestCase):

    def test_selectedApplication(self):
        from scrolls.log import Log
        log = Log(self.dependencies)
        log.selectedApplication(name='abc', logfile='/p/abc.log')
