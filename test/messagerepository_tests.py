from test.ditestcase import DITestCase
from mock import Mock


class MessageRepositoryTests(DITestCase):

    def test_add_sorts_messages(self):
        from scrolls.repositories.message import MessageRepository
        self.filesys.readJson.return_value = [
            (1, 'a msg'),
            (3, 'a msg'),
        ]
        messages = MessageRepository(self.dependencies)
        messages.add([
            self.messageWithTimestamp(2),
            self.messageWithTimestamp(4),
        ])
        saved = self.filesys.writeJson.call_args[0][1]
        self.assertEqual([
            (1, 'a msg'),
            (2, 'a msg'),
            (3, 'a msg'),
            (4, 'a msg')
        ], saved)

    def test_add_limits_database_to_1000_records(self):
        from scrolls.repositories.message import MessageRepository
        self.filesys.readJson.return_value = [(888, 'a msg')] * 600
        messages = MessageRepository(self.dependencies)
        messages.add([self.messageWithTimestamp(999)] * 600)
        saved = self.filesys.writeJson.call_args[0][1]
        self.assertEqual(len(saved), 1000)

    def test_getLatest(self):
        from scrolls.repositories.message import MessageRepository
        self.message.fromTuple.side_effect = lambda t: ('M', t[0], t[1])
        messages = MessageRepository(self.dependencies)
        self.filesys.readJson.return_value = [(n, str(n)) for n in range(10)]
        self.assertEqual(messages.getLatest(3), [
            ('M', 7, '7'),
            ('M', 8, '8'),
            ('M', 9, '9')
        ])

    def messageWithTimestamp(self, ts):
        msg = Mock()
        msg.toTuple.return_value = (ts, 'a msg')
        return msg
