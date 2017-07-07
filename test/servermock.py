from mock import Mock


class MockServer(object):  # stand in for socketserver.TCPServer

    def __init__(self, clock):
        self.clock = clock
        self.rfile = Mock()
        self.requests_handled = 0
        self.secondsToAdvanceClockPerRequest = 1
        self.raiseKeyboardInterruptOnRequestNo = 99
        self.timeOutOnRequestNo = -1

    def handle_request(self):
        self.requests_handled += 1
        handler = self.Handler()
        handler.server = self
        if self.requests_handled >= self.raiseKeyboardInterruptOnRequestNo:
            raise KeyboardInterrupt
        self.clock.advance(self.secondsToAdvanceClockPerRequest)
        if self.requests_handled == self.timeOutOnRequestNo:
            handler.handle_timeout()
            return
        msg = 'msg' + str(self.requests_handled)
        handler.rfile = Mock()
        handler.rfile.read.return_value = msg
        handler.client_address = [msg + 'client']
        handler.handle()
