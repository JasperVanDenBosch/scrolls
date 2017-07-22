from scrolls.clock import Clock
from scrolls.configuration import Configuration
from scrolls.factories.counter import CounterFactory
from scrolls.factories.message import MessageFactory
from scrolls.filesystem import Filesystem
from scrolls.log import Log
from scrolls.importer import MessageImporter
from scrolls.repositories.message import MessageRepository
from scrolls.rsyslog import RSyslog
from scrolls.security import Security
from scrolls.server import Server
from scrolls.repositories.statistic import StatisticRepository


class Dependencies(object):
    """
    Dependency Injection service.
    """
    def __init__(self, request=None):
        self.config = None
        self.request = request

    def getClock(self):
        return Clock()

    def getConfiguration(self):
        if self.config is None:
            self.config = Configuration(self)
        return self.config

    def getCounterFactory(self):
        return CounterFactory(self)

    def getFilesystem(self):
        return Filesystem(self)

    def getListener(self):
        import scrolls.listener
        from socketserver import UDPServer
        return scrolls.listener.Listener(UDPServer, self)

    def getLog(self):
        return Log(self)

    def getMessageFactory(self):
        return MessageFactory(self, self.request)

    def getMessageImporter(self):
        return MessageImporter(self)

    def getMessageRepository(self):
        return MessageRepository(self)

    def getRSyslog(self):
        return RSyslog(self)

    def getSecurity(self):
        return Security(self)

    def getServer(self):
        return Server(self)

    def getStatisticRepository(self):
        return StatisticRepository(self)

    def withRequest(self, request):
        return Dependencies(request)
