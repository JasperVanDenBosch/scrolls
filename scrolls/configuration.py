

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

    password_secret = 'papyrus'
    """str: Any string you choose. This is used to encrypt your password.
    You can generate this by running `scrolls generate-secrets`."""

    ticket_secret = 'Herculaneum'
    """str: Any string you choose. This is used to encrypt the auth cookie.
    You can generate this by running `scrolls generate-secrets`."""

    hashed_password = ''
    """str: The sha256 hash of the concatenation of your password and the
    password_secret. You can generate this by running
    `scrolls generate-secrets`."""

    def __init__(self, dependencies):
        pass

    def useCommandlineArgs(self, args):
        if hasattr(args, 'server'):
            self.server = args.server
