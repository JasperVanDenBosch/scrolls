from mock import Mock


class MockServer(object):  # stand in for socketserver.TCPServer

    def __init__(self, clock):
        self.clock = clock
        self.rfile = Mock()
        self.requests_handled = 0
        self.secondsToAdvanceClockPerRequest = 1
        self.raiseKeyboardInterruptOnRequestNo = 99

    def handle_request(self):
        self.requests_handled += 1
        handler = self.Handler()
        handler.server = self
        if self.requests_handled >= self.raiseKeyboardInterruptOnRequestNo:
            raise KeyboardInterrupt
        self.clock.advance(self.secondsToAdvanceClockPerRequest)
        msg = 'msg' + str(self.requests_handled)
        handler.rfile = Mock()
        handler.rfile.read.return_value = msg
        handler.client_address = [msg + 'client']
        handler.handle()
