from scrolls.models.message import Message


class MessageFactory(object):
    """Responsible for creating Message objects.

    See :class:`scrolls.models.message.Message`
    """

    def __init__(self, dependencies, request=None):
        self.security = dependencies.getSecurity()
        self.parser = dependencies.getRSyslogParser()
        self.request = request

    def parseFrom(self, rsyslogString, withId=None):
        """Create a Message by parsing the rsyslog data string

        If no pre-made id is passed as `withId`, a new one is generated.
        """
        if withId is None:
            withId = self.security.generateShortUuid()
        mdict = self.parser.parse(rsyslogString)
        mdict.update({'id': withId})
        newMessage = Message(mdict)
        if self.request:
            newMessage.resourcify(parent=self.request.root.getIdResolver())
        return newMessage
