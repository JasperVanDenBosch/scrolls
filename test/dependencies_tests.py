from unittest import TestCase


class DependenciesTests(TestCase):

    def test_getClock(self):
        from scrolls.dependencies import Dependencies
        from scrolls.clock import Clock
        dependencies = Dependencies()
        dependency = dependencies.getClock()
        self.assertIsInstance(dependency, Clock)

    def test_getMessageRepository(self):
        from scrolls.dependencies import Dependencies
        from scrolls.repositories.message import MessageRepository
        dependencies = Dependencies()
        dependency = dependencies.getMessageRepository()
        self.assertIsInstance(dependency, MessageRepository)

    def test_getListener(self):
        from scrolls.dependencies import Dependencies
        from scrolls.listener import Listener
        dependencies = Dependencies()
        dependency = dependencies.getListener()
        self.assertIsInstance(dependency, Listener)
