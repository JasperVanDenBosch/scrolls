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
        mdict = self.parser.parse(rsyslogString)
        if withId is None:
            withId = self.createId(mdict)
        mdict.update({'id': withId})
        newMessage = Message(mdict)
        if self.request:
            newMessage.resourcify(parent=self.request.root.getIdResolver())
        return newMessage

    def createId(self, mdict):
        """Create an ID for the message based on dictionary mdict.

        The id is a combination of the timestamp and a 6 character unique id.
        """
        suid = self.security.generateShortUuid()
        dtstr = mdict['datetime'].strftime('%Y%m%d%H%M%S%f')[:-3]
        return dtstr + suid
