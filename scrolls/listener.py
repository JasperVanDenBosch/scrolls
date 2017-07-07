

class Listener(object):

    def __init__(self, serverClass, dependencies):
        self.serverClass = serverClass
        self.clock = dependencies.getClock()
        self.messages = dependencies.getMessageRepository()

    def listen(self):
        class Handler(object):
            def handle(self):
                pass
        nextFlushTime = self.clock.time() + 0.05
        server = self.serverClass(("0.0.0.0", 514), Handler)
        while True:
            try:
                server.handle_request()
                if self.clock.time() > nextFlushTime:
                    self.messages.add()
                    nextFlushTime = self.clock.time() + 0.05
            except KeyboardInterrupt:
                break
