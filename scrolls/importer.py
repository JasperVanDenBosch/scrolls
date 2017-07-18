

class MessageImporter(object):
    """Deals with newly arrived Messages"""

    def __init__(self, dependencies):
        self.repository = dependencies.getMessageRepository()

    def import_(self, messages):
        """Handles a batch of new messages

        Will persist and aggregate them. If the batch is empty, will return
        immediately.

        Args:
            messages (list): List of Message objects to be imported.
        """
        if messages == []:
            return
        self.repository.add(messages)
