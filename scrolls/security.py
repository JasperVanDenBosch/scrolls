import hashlib
import string
import random


class Security(object):

    def __init__(self, dependencies):
        self.config = dependencies.getConfiguration()

    def hashPassword(self, password, secret=None):
        if secret is None:
            secret = self.config.password_secret
        secretpw = secret + password
        return hashlib.sha256(secretpw.encode('utf-8')).hexdigest()

    def generateSecret(self):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        charlist = [random.SystemRandom().choice(chars) for _ in range(24)]
        return ''.join(charlist)

    def generateSecrets(self, password):
        secrets = {'ticket_secret': '', 'password_secret': '',
                   'hashed_password': ''}
        if not password == '':
            secrets['ticket_secret'] = self.generateSecret()
            pwSecret = self.generateSecret()
            secrets['password_secret'] = pwSecret
            secrets['hashed_password'] = self.hashPassword(password, pwSecret)
        return secrets
