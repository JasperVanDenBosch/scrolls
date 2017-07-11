from test.ditestcase import DITestCase


class MessageRepositoryTests(DITestCase):

    def test_addFrom(self):
        from scrolls.repositories.message import MessageRepository
        messages = MessageRepository(self.dependencies)
        self.assertIsNotNone(messages)

    def test_add_sorts_messages(self):
        from scrolls.repositories.message import MessageRepository
        self.filesys.readJson.return_value = [
            ('1', '<54>1 2017-01-11T14:44:37.992647+01:00 - - - - -  hallo\n'),
            ('3', '<13>1 2017-03-11T14:44:37.992647+01:00 - - - - -  hallo\n'),
        ]
        messages = MessageRepository(self.dependencies)
        messages.add([
            ('2', '<34>1 2017-02-11T14:44:37.992647+01:00 - - - - -  hallo\n'),
            ('4', '<11>1 2017-04-11T14:44:37.992647+01:00 - - - - -  hallo\n'),
        ])
        saved = self.filesys.writeJson.call_args[0][1]
        self.assertEqual([
            ('1', '<54>1 2017-01-11T14:44:37.992647+01:00 - - - - -  hallo\n'),
            ('2', '<34>1 2017-02-11T14:44:37.992647+01:00 - - - - -  hallo\n'),
            ('3', '<13>1 2017-03-11T14:44:37.992647+01:00 - - - - -  hallo\n'),
            ('4', '<11>1 2017-04-11T14:44:37.992647+01:00 - - - - -  hallo\n'),
        ], saved)

    def test_add_limits_database_to_1000_records(self):
        from scrolls.repositories.message import MessageRepository
        m = ('1', '<54>1 2017-01-11T14:44:37.992647+01:00 - - - - -  hallo\n')
        self.filesys.readJson.return_value = [m] * 600
        messages = MessageRepository(self.dependencies)
        messages.add([m] * 600)
        saved = self.filesys.writeJson.call_args[0][1]
        self.assertEqual(len(saved), 1000)

    def test_getLatest(self):
        from scrolls.repositories.message import MessageRepository
        messages = MessageRepository(self.dependencies)
        self.filesys.readJson.return_value = list(range(10))
        self.assertEqual(messages.getLatest(3), [7, 8, 9])
