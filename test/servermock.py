

class MockServer(object):  # stand in for socketserver.TCPServer

    def __init__(self, clock):
        self.clock = clock
        self.requests_handled = 0
        self.secondsToAdvanceClockPerRequest = 1
        self.raiseKeyboardInterruptOnRequestNo = 99

    def handle_request(self):
        self.requests_handled += 1
        if self.requests_handled >= self.raiseKeyboardInterruptOnRequestNo:
            raise KeyboardInterrupt
        msg = 'msg' + str(self.requests_handled)
        # request.makefile().read.return_value = msg # for tcp streamhandler
        req = [msg.encode('utf-8')]
        self.Handler(request=req, client_address=[msg + 'client'], server=self)
        self.clock.advance(self.secondsToAdvanceClockPerRequest)
