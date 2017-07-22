from test.ditestcase import DITestCase
from datetime import datetime
from mock import Mock, sentinel
from dateutil.tz import tzoffset


class MessageTests(DITestCase):

    def test_dt_syslog(self):
        from scrolls.models.message import Message
        data = '<54>1 2017-01-11T14:44:37.992647+01:00 - - - - -  hallo\n'
        dt = datetime(2017, 1, 11, 14, 44, 37, 992647,
                      tzinfo=tzoffset(None, 3600))
        message = Message('client', data, 'xyz')
        self.assertEqual(message.getDatetime(), dt)

    def test_timestamp(self):
        from scrolls.models.message import Message
        dt = datetime(2017, 1, 11, 14, 44, 37, 992647,
                      tzinfo=tzoffset(None, 3600))
        message = Message('client', 'data', 'xyz')
        message.getDatetime = Mock()
        message.getDatetime.return_value = dt
        self.assertEqual(message.getTimestamp(), dt.timestamp())

    def test_id(self):
        from scrolls.models.message import Message
        dt = datetime(2017, 1, 11, 14, 44, 37, 992647,
                      tzinfo=tzoffset(None, 3600))
        message = Message('client', 'data', 'abcdef')
        message.getDatetime = Mock()
        message.getDatetime.return_value = dt
        self.assertEqual(message.getId(), '20170111144437992abcdef')

    def test_toTuple(self):
        from scrolls.models.message import Message
        message = Message('client', 'data', 'xyz')
        message.getTimestamp = Mock()
        message.getTimestamp.return_value = 123.456
        self.assertEqual(message.toTuple(), (
            123.456, 'client', 'data', 'xyz'
        ))

    def test_hostname(self):
        from scrolls.models.message import Message
        data = ('<38>1 2017-07-18T00:36:21.238521+00:00 www sshd 11943 ' +
                '- - Received disconnect from 59.45.175.67\n')
        message = Message('client', data, 'xyz')
        self.assertEqual(message.getHostname(), 'www')

    def test_app(self):
        from scrolls.models.message import Message
        data = ('<38>1 2017-07-18T00:36:21.238521+00:00 www sshd 11943 ' +
                '- - Received disconnect from 59.45.175.67\n')
        message = Message('client', data, 'xyz')
        self.assertEqual(message.getApp(), 'sshd')

    def test_content(self):
        from scrolls.models.message import Message
        data = ('<38>1 2017-07-18T00:36:21.238521+00:00 www sshd 11943 ' +
                '- - Received disconnect from 59.45.175.67\n')
        message = Message('client', data, 'xyz')
        self.assertEqual(message.getContent(),
                         'Received disconnect from 59.45.175.67')

    def test_toDict(self):
        from scrolls.models.message import Message
        data = ('<38>1 2017-07-18T00:36:21.238521+00:00 www sshd 11943 ' +
                '- - Received disconnect from 59.45.175.67\n')
        dt = datetime(2017, 7, 18, 00, 36, 21, 238521,
                      tzinfo=tzoffset(None, 0))
        message = Message('client', data, 'xyz')
        self.assertEqual(message.toDict(), {
            'datetime': dt,
            'hostname': 'www',
            'app': 'sshd',
            'content': 'Received disconnect from 59.45.175.67',
        })

    def test_resourcify(self):
        from scrolls.models.message import Message
        message = Message('client', 'data', 'xyz')
        message.getId = Mock()
        message.resourcify(parent=sentinel.parent)
        self.assertEqual(message.__parent__, sentinel.parent)
        self.assertEqual(message.__name__, message.getId())
