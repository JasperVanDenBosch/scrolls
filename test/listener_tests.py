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

    def test_saves_after_50ms_passed(self):
        from scrolls.listener import Listener
        self.server.secondsToAdvanceClockPerRequest = .01
        self.server.raiseKeyboardInterruptOnRequestNo = 9
        listener = Listener(self.ServerClass, self.dependencies)
        listener.listen()
        self.assertEqual(self.messages.add.call_count, 1)

    def test_saves_if_request_times_out(self):
        from scrolls.listener import Listener
        self.server.secondsToAdvanceClockPerRequest = .01
        self.server.timeOutOnRequestNo = 4
        self.server.raiseKeyboardInterruptOnRequestNo = 7
        listener = Listener(self.ServerClass, self.dependencies)
        listener.listen()
        self.assertEqual(self.messages.add.call_count, 1)
