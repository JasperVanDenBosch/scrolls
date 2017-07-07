from scrolls.clock import Clock
from scrolls.repositories.message import MessageRepository


class Dependencies(object):
    """
    Dependency Injection service.
    """

    def getClock(self):
        return Clock()

    def getMessageRepository(self):
        return MessageRepository()
