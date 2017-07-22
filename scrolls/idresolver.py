

class IdResolver(object):

    def __init__(self, parent, dependencies):
        self.__parent__ = parent
        self.__name__ = 'id'
        self.messages = dependencies.getMessageRepository()

    def __getitem__(self, key):
        message = self.messages.getById(key)
        if message:
            return message
        else:
            raise KeyError
