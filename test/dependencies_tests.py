from unittest import TestCase


class DependenciesTests(TestCase):

    def test_getClock(self):
        from scrolls.dependencies import Dependencies
        from scrolls.clock import Clock
        dependencies = Dependencies()
        dependency = dependencies.getClock()
        self.assertIsInstance(dependency, Clock)

    def test_getConfiguration(self):
        from scrolls.dependencies import Dependencies
        from scrolls.configuration import Configuration
        dependencies = Dependencies()
        dependency = dependencies.getConfiguration()
        self.assertIsInstance(dependency, Configuration)

    def test_getFilesystem(self):
        from scrolls.dependencies import Dependencies
        from scrolls.filesystem import Filesystem
        dependencies = Dependencies()
        dependency = dependencies.getFilesystem()
        self.assertIsInstance(dependency, Filesystem)

    def test_getListener(self):
        from scrolls.dependencies import Dependencies
        from scrolls.listener import Listener
        dependencies = Dependencies()
        dependency = dependencies.getListener()
        self.assertIsInstance(dependency, Listener)

    def test_getLog(self):
        from scrolls.dependencies import Dependencies
        from scrolls.log import Log
        dependencies = Dependencies()
        dependency = dependencies.getLog()
        self.assertIsInstance(dependency, Log)

    def test_getMessageFactory(self):
        from scrolls.dependencies import Dependencies
        from scrolls.factories.message import MessageFactory
        dependencies = Dependencies()
        dependency = dependencies.getMessageFactory()
        self.assertIsInstance(dependency, MessageFactory)

    def test_getMessageRepository(self):
        from scrolls.dependencies import Dependencies
        from scrolls.repositories.message import MessageRepository
        dependencies = Dependencies()
        dependency = dependencies.getMessageRepository()
        self.assertIsInstance(dependency, MessageRepository)

    def test_getRSyslog(self):
        from scrolls.dependencies import Dependencies
        from scrolls.rsyslog import RSyslog
        dependencies = Dependencies()
        dependency = dependencies.getRSyslog()
        self.assertIsInstance(dependency, RSyslog)

    def test_getSecurity(self):
        from scrolls.dependencies import Dependencies
        from scrolls.security import Security
        dependencies = Dependencies()
        dependency = dependencies.getSecurity()
        self.assertIsInstance(dependency, Security)

    def test_getServer(self):
        from scrolls.dependencies import Dependencies
        from scrolls.server import Server
        dependencies = Dependencies()
        dependency = dependencies.getServer()
        self.assertIsInstance(dependency, Server)
