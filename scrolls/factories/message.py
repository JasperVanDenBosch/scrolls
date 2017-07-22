from scrolls.models.message import Message


class MessageFactory(object):
    """Responsible for creating Message objects.

    See :class:`scrolls.models.message.Message`
    """

    def __init__(self, dependencies, request=None):
        self.security = dependencies.getSecurity()
        self.request = request

    def fromTuple(self, mtuple):
        """Create a Message from a 2-tuple or a 3-tuple

        If a 3-tuple is passed, the first element, presumed to be
        the timestamp, is discarded.
        """
        if len(mtuple) > 2:
            mtuple = mtuple[1:]
        else:
            mtuple += (self.security.generateShortUuid(),)
        newMessage = Message(*mtuple)
        if self.request:
            newMessage.resourcify(parent=self.request.root.getIdResolver())
        return newMessage
