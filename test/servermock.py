from mock import Mock


class MockServer(object):  # stand in for socketserver.TCPServer

    def __init__(self, clock):
        self.clock = clock
        self.rfile = Mock()
        self.client_address = ['MockClientAddress']
        self.requests_handled = 0
        self.secondsToAdvanceClockPerRequest = 1
        self.raiseKeyboardInterruptOnRequestNo = 99

    def handle_request(self):
        self.requests_handled += 1
        if self.requests_handled >= self.raiseKeyboardInterruptOnRequestNo:
            raise KeyboardInterrupt
        self.rfile.read.return_value = 'msg' + str(self.requests_handled)
        self.clock.advance(self.secondsToAdvanceClockPerRequest)
        handler = self.Handler()
        handler.server = self
        handler.handle()
