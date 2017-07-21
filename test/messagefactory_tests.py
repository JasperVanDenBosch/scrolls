from test.ditestcase import DITestCase
from mock import patch


class MessageFactoryTests(DITestCase):

    def test_2tuple(self):
        from scrolls.factories.message import MessageFactory
        ids = ['def', 'abc']
        self.security.generateShortUuid.side_effect = lambda: ids.pop()
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            msg = factory.fromTuple(('client', 'data'))
            Message.assert_called_with('client', 'data', 'abc')
            self.assertEqual(msg, Message())
            msg = factory.fromTuple(('client', 'data'))
            Message.assert_called_with('client', 'data', 'def')

    def test_3tuple(self):
        from scrolls.factories.message import MessageFactory
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            msg = factory.fromTuple((123, 'client', 'data'))
            Message.assert_called_with('client', 'data')
            self.assertEqual(msg, Message())
