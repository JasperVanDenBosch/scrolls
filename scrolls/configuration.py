

class Configuration(object):
    """General settings for Scrolls.

    Individual settings are documented as follows;

    **setting** *= default_value*
        *type* - Explanation.

    The settings can be changed in the configuration file, in code, or
    by passing an ArgParser-like object of commandline arguments to
    useCommandlineArgs().

    All settings:
    """

    server = '0.0.0.0'
    """str: URL of the log server."""

    def __init__(self, dependencies):
        pass

    def useCommandlineArgs(self, args):
        if hasattr(args, 'server'):
            self.server = args.server
