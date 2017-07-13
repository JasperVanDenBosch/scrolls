import hashlib


class Security(object):

    def __init__(self, dependencies):
        self.config = dependencies.getConfiguration()

    def hashPassword(self, password):
        secretpw = self.config.password_secret + password
        return hashlib.sha256(secretpw.encode('utf-8')).hexdigest()
