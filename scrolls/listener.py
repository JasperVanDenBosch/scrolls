

class Listener(object):

    def __init__(self, serverClass, dependencies):
        self.serverClass = serverClass
        self.clock = dependencies.getClock()
        self.messages = dependencies.getMessageRepository()

    def listen(self):
        class Handler(object):
            def handle(self):
                pass
            def handle_timeout(self):
                self.server.timed_out = True

        nextFlushTime = self.clock.time() + 0.05
        server = self.serverClass(("0.0.0.0", 514), Handler)
        server.timed_out = False
        while True:
            try:
                server.handle_request()
                if self.clock.time() > nextFlushTime or server.timed_out:
                    self.messages.add()
                    server.timed_out = False
                    nextFlushTime = self.clock.time() + 0.05
            except KeyboardInterrupt:
                break
