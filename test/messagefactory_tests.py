from test.ditestcase import DITestCase
from mock import patch, Mock


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
            factory.fromTuple(('client', 'data'))
            Message.assert_called_with('client', 'data', 'def')

    def test_4tuple(self):
        from scrolls.factories.message import MessageFactory
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            msg = factory.fromTuple((123, 'client', 'data', 'abc'))
            Message.assert_called_with('client', 'data', 'abc')
            self.assertEqual(msg, Message())

    def test_resourcifies_if_has_request(self):
        from scrolls.factories.message import MessageFactory
        request = Mock()
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies, request)
            factory.fromTuple((123, 'client', 'data', 'abc'))
            Message().resourcify.assert_called_with(
                parent=request.root.getIdResolver()
            )
            factory.fromTuple(('client', 'data'))
            Message().resourcify.assert_called_with(
                parent=request.root.getIdResolver()
            )
