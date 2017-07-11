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
