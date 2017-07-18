from test.ditestcase import DITestCase
from test.servermock import MockServer


class ListenerTests(DITestCase):

    def setUp(self):
        super(ListenerTests, self).setUp()
        self.server = MockServer(self.clock)

        def ServerClass(_, Handler):
            self.server.Handler = Handler
            return self.server
        self.ServerClass = ServerClass

    def test_listen_catches_keyboard_interrupts(self):
        from scrolls.listener import Listener
        self.server.raiseKeyboardInterruptOnRequestNo = 9
        listener = Listener(self.ServerClass, self.dependencies)
        try:
            listener.listen()
        except KeyboardInterrupt:
            self.fail('KeyboardInterrupt passed through.')
        self.assertEqual(self.server.requests_handled, 9)

    def test_flushes_after_50ms_passed(self):
        from scrolls.listener import Listener
        self.message.fromTuple.side_effect = lambda t: ('M', t[0], t[1])
        self.server.secondsToAdvanceClockPerRequest = .01
        self.server.raiseKeyboardInterruptOnRequestNo = 9
        listener = Listener(self.ServerClass, self.dependencies)
        listener.listen()
        self.assertEqual(self.importer.import_.call_count, 1)
        self.importer.import_.assert_called_with([
            ('M', 'msg1client', 'msg1'),
            ('M', 'msg2client', 'msg2'),
            ('M', 'msg3client', 'msg3'),
            ('M', 'msg4client', 'msg4'),
            ('M', 'msg5client', 'msg5'),
        ])
