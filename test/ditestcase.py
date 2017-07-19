from unittest import TestCase
from mock import Mock
from test.clockmock import ClockMock


class DITestCase(TestCase):

    def setUp(self):
        deps = Mock()
        self.clock = ClockMock()
        self.messages = Mock()
        self.config = Mock()
        self.rsyslog = Mock()
        self.filesys = Mock()
        self.server = Mock()
        self.security = Mock()
        self.log = Mock()
        self.security.hashPassword = lambda p: p + '+secret'
        self.message = Mock()
        self.importer = Mock()
        self.stats = Mock()
        self.count = Mock()
        deps.getMessageRepository.return_value = self.messages
        deps.getClock.return_value = self.clock
        deps.getConfiguration.return_value = self.config
        deps.getRSyslog.return_value = self.rsyslog
        deps.getFilesystem.return_value = self.filesys
        deps.getServer.return_value = self.server
        deps.getSecurity.return_value = self.security
        deps.getLog.return_value = self.log
        deps.getMessageFactory.return_value = self.message
        deps.getMessageImporter.return_value = self.importer
        deps.getStatisticRepository.return_value = self.stats
        deps.getCounterFactory.return_value = self.count
        self.dependencies = deps
