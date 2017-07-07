from unittest import TestCase
from mock import Mock


class ListenerTests(TestCase):

    def test_listen(self):
        from scrolls.listener import Listener
        ServerClass = Mock() # stand in for socketserver.TCPServer
        listener = Listener(ServerClass)
        listener.listen()


# if timeout, save cacge
# after polling time, saves messages


