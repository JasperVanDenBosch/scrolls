from test.ditestcase import DITestCase
from mock import sentinel


class IdResolverTests(DITestCase):

    def test_resource(self):
        from scrolls.idresolver import IdResolver
        resolver = IdResolver(sentinel.parent, self.dependencies)
        self.assertEqual(resolver.__name__, 'id')
        self.assertEqual(resolver.__parent__, sentinel.parent)

    def test_throws_keyerror_if_repo_doesnt_know_id(self):
        from scrolls.idresolver import IdResolver
        self.messages.getById.return_value = None
        resolver = IdResolver(None, self.dependencies)
        with self.assertRaises(KeyError):
            resolver['nothing']

    def test_returns_message_from_repo(self):
        from scrolls.idresolver import IdResolver
        self.messages.getById.return_value = sentinel.message
        resolver = IdResolver(None, self.dependencies)
        self.assertEqual(resolver['theid'], sentinel.message)
