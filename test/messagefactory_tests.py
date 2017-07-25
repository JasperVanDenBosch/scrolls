from test.ditestcase import DITestCase
from mock import patch, Mock
import datetime


class MessageFactoryTests(DITestCase):

    def setUp(self):
        super(MessageFactoryTests, self).setUp()
        dt = datetime.datetime.now()
        self.rsyslogParser.parse.return_value = {'datetime': dt}
        self.security.generateShortUuid.return_value = 'xyz'

    def test_without_id_generates_it(self):
        from scrolls.factories.message import MessageFactory
        ids = ['def', 'abc']
        self.security.generateShortUuid.side_effect = lambda: ids.pop()
        dt = datetime.datetime(2017, 1, 11, 14, 44, 37, 992647)
        self.rsyslogParser.parse.return_value = {'datetime': dt}
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            factory.parseFrom('data')
            mdict = Message.call_args[0][0]
            self.assertEqual(mdict['id'], '20170111144437992abc')
            factory.parseFrom('data')
            mdict = Message.call_args[0][0]
            self.assertEqual(mdict['id'], '20170111144437992def')

    def test_with_id_uses_it(self):
        from scrolls.factories.message import MessageFactory
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            factory.parseFrom('data', withId='123xyz')
            mdict = Message.call_args[0][0]
            self.assertEqual(mdict['id'], '123xyz')

    def test_uses_parser(self):
        from scrolls.factories.message import MessageFactory
        self.rsyslogParser.parse.return_value['abc'] = 123
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies)
            factory.parseFrom('rsyslog data string')
            self.rsyslogParser.parse.assert_called_with('rsyslog data string')
            mdict = Message.call_args[0][0]
            self.assertIn('abc', mdict)
            self.assertEqual(mdict['abc'], 123)

    def test_resourcifies_if_has_request(self):
        from scrolls.factories.message import MessageFactory
        request = Mock()
        with patch('scrolls.factories.message.Message') as Message:
            factory = MessageFactory(self.dependencies, request)
            factory.parseFrom('data')
            Message().resourcify.assert_called_with(
                parent=request.root.getIdResolver()
            )
