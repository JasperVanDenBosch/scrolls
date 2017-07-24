from test.ditestcase import DITestCase
from mock import patch, Mock


class MessageFactoryTests(DITestCase):

    def test_without_id_generates_it(self):
        from scrolls.factories.message import MessageFactory
        ids = ['def', 'abc']
        self.security.generateShortUuid.side_effect = lambda: ids.pop()
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            factory.parseFrom('data')
            mdict = Message.call_args[0][0]
            self.assertEqual(mdict['id'], 'abc')
            factory.parseFrom('data')
            mdict = Message.call_args[0][0]
            self.assertEqual(mdict['id'], 'def')

    def test_with_id_uses_it(self):
        from scrolls.factories.message import MessageFactory
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            factory.parseFrom('data', withId='123xyz')
            mdict = Message.call_args[0][0]
            self.assertEqual(mdict['id'], '123xyz')

    def test_resourcifies_if_has_request(self):
        from scrolls.factories.message import MessageFactory
        request = Mock()
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies, request)
            factory.parseFrom('data')
            Message().resourcify.assert_called_with(
                parent=request.root.getIdResolver()
            )
            factory.parseFrom(('client', 'data'))
            Message().resourcify.assert_called_with(
                parent=request.root.getIdResolver()
            )
