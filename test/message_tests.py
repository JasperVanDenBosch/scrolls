from test.ditestcase import DITestCase
from mock import Mock, sentinel


class MessageTests(DITestCase):

    def test_id(self):
        from scrolls.models.message import Message
        mdict = {'id': '123abc'}
        message = Message(mdict)
        self.assertEqual(message.getId(), '123abc')

    def test_data(self):
        from scrolls.models.message import Message
        mdict = {'data': sentinel.data}
        message = Message(mdict)
        self.assertEqual(message.getData(), sentinel.data)

    def test_datetime(self):
        from scrolls.models.message import Message
        mdict = {'datetime': sentinel.datetime}
        message = Message(mdict)
        self.assertEqual(message.getDatetime(), sentinel.datetime)

    def test_toDict(self):
        from scrolls.models.message import Message
        mdict = {'id': '123abc'}
        message = Message(mdict)
        self.assertEqual(message.toDict(), mdict)

    def test_resourcify(self):
        from scrolls.models.message import Message
        message = Message({})
        message.getId = Mock()
        message.resourcify(parent=sentinel.parent)
        self.assertEqual(message.__parent__, sentinel.parent)
        self.assertEqual(message.__name__, message.getId())
