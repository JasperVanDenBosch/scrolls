from socketserver import BaseRequestHandler


class Listener(object):

    def __init__(self, serverClass, dependencies):
        self.serverClass = serverClass
        self.clock = dependencies.getClock()
        self.messages = dependencies.getMessageImporter()
        self.message = dependencies.getMessageFactory()

    def listen(self):

        class Handler(BaseRequestHandler):
            def handle(self):
                data = self.request[0].decode()
                client = self.client_address[0]
                self.server.cache.append((client, data))

        nextFlushTime = self.clock.time() + 0.05
        server = self.serverClass(("0.0.0.0", 8514), Handler)
        server.timeout = 0.05
        server.cache = []
        while True:
            try:
                server.handle_request()
                if self.clock.time() >= nextFlushTime:
                    self.flushCache(server)
                    nextFlushTime = self.clock.time() + 0.05
            except KeyboardInterrupt:
                break

    def flushCache(self, server):
        nCached = len(server.cache)
        tuples = list(reversed([server.cache.pop() for _ in range(nCached)]))
        newMessages = [self.message.fromTuple(t) for t in tuples]
        self.messages.import_(newMessages)
