from test.ditestcase import DITestCase
from datetime import datetime
from mock import Mock
from dateutil.tz import tzoffset
import time


class MessageTests(DITestCase):

    def test_dt_syslog(self):
        from scrolls.models.message import Message
        data = '<54>1 2017-01-11T14:44:37.992647+01:00 - - - - -  hallo\n'
        dt = datetime(2017, 1, 11, 14, 44, 37, 992647,
                      tzinfo=tzoffset(None, 3600))
        message = Message('client', data)
        self.assertEqual(message.getDatetime(), dt)

    def test_timestamp(self):
        from scrolls.models.message import Message
        dt = datetime(2017, 1, 11, 14, 44, 37, 992647,
                      tzinfo=tzoffset(None, 3600))
        message = Message('client', 'data')
        message.getDatetime = Mock()
        message.getDatetime.return_value = dt
        self.assertEqual(message.getTimestamp(), dt.timestamp())

    def test_toTuple(self):
        from scrolls.models.message import Message
        message = Message('client', 'data')
        message.getTimestamp = Mock()
        message.getTimestamp.return_value = 123.456
        self.assertEqual(message.toTuple(), (
            123.456, 'client', 'data'
        ))

