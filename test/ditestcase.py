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
        deps.getMessageRepository.return_value = self.messages
        deps.getClock.return_value = self.clock
        deps.getConfiguration.return_value = self.config
        deps.getRSyslog.return_value = self.rsyslog
        deps.getFilesystem.return_value = self.filesys
        deps.getServer.return_value = self.server
        self.dependencies = deps
