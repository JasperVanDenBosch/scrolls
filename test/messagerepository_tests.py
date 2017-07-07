from unittest import TestCase


class MessageRepositoryTests(TestCase):

    def test_addFrom(self):
        from scrolls.repositories.message import MessageRepository
        messages = MessageRepository()
        self.assertIsNotNone(messages)
