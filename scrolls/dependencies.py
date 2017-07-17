from scrolls.clock import Clock
from scrolls.configuration import Configuration
from scrolls.filesystem import Filesystem
from scrolls.log import Log
from scrolls.repositories.message import MessageRepository
from scrolls.rsyslog import RSyslog
from scrolls.security import Security
from scrolls.server import Server


class Dependencies(object):
    """
    Dependency Injection service.
    """
    def __init__(self):
        self.config = None

    def getClock(self):
        return Clock()

    def getConfiguration(self):
        if self.config is None:
            self.config = Configuration(self)
        return self.config

    def getFilesystem(self):
        return Filesystem(self)

    def getListener(self):
        import scrolls.listener
        from socketserver import UDPServer
        return scrolls.listener.Listener(UDPServer, self)

    def getLog(self):
        return Log(self)

    def getMessageRepository(self):
        return MessageRepository(self)

    def getRSyslog(self):
        return RSyslog(self)

    def getSecurity(self):
        return Security(self)

    def getServer(self):
        return Server(self)
