from test.ditestcase import DITestCase


class SecurityTests(DITestCase):

    def test_hash(self):
        from scrolls.security import Security
        self.config.password_secret = 'secret'
        security = Security(self.dependencies)
        self.assertEqual(security.hashPassword('ab12'),
                         security.hashPassword('ab12'))
        self.assertNotEqual(security.hashPassword('ab12'),
                            security.hashPassword('ac12'))
        self.assertGreater(len(security.hashPassword('a')), 63)
