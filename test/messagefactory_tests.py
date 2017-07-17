from test.ditestcase import DITestCase
from mock import patch


class MessageFactoryTests(DITestCase):

    def test_2tuple(self):
        from scrolls.factories.message import MessageFactory
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            msg = factory.fromTuple(('client', 'data'))
            Message.assert_called_with('client', 'data')
            self.assertEqual(msg, Message())

    def test_3tuple(self):
        from scrolls.factories.message import MessageFactory
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            msg = factory.fromTuple((123, 'client', 'data'))
            Message.assert_called_with('client', 'data')
            self.assertEqual(msg, Message())
