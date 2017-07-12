from scrolls.clock import Clock
from scrolls.configuration import Configuration
from scrolls.filesystem import Filesystem
from scrolls.repositories.message import MessageRepository
from scrolls.rsyslog import RSyslog
from scrolls.server import Server


class Dependencies(object):
    """
    Dependency Injection service.
    """

    def getClock(self):
        return Clock()

    def getConfiguration(self):
        return Configuration(self)

    def getFilesystem(self):
        return Filesystem(self)

    def getListener(self):
        import scrolls.listener
        from socketserver import UDPServer
        return scrolls.listener.Listener(UDPServer, self)

    def getMessageRepository(self):
        return MessageRepository(self)

    def getRSyslog(self):
        return RSyslog(self)

    def getServer(self):
        return Server(self)
