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
        self.assertGreaterEqual(len(security.hashPassword('a')), 64)

    def test_generateSecret(self):
        from scrolls.security import Security
        security = Security(self.dependencies)
        MINLENGTH = 24
        self.assertGreaterEqual(len(security.generateSecret()), MINLENGTH)
        self.assertNotEqual(security.generateSecret(),
                            security.generateSecret())
        secret = security.generateSecret()
        nUpper = sum([c.isupper() for c in secret])
        nDigits = sum([c.isdigit() for c in secret])
        self.assertGreater(nUpper, 0)
        self.assertLess(nUpper, len(secret))
        self.assertGreater(nDigits, 0)
        self.assertLess(nDigits, len(secret))
