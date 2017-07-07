from unittest import TestCase
from mock import Mock
from test.clockmock import ClockMock


class DITestCase(TestCase):

    def setUp(self):
        deps = Mock()
        self.clock = ClockMock()
        self.messages = Mock()
        deps.getMessageRepository.return_value = self.messages
        deps.getClock.return_value = self.clock
        self.dependencies = deps
