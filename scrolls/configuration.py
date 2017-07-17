import configparser
import os


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

    dry_run = False
    """bool: Simulate configure() but don't make filesystem changes."""

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
        self._dependencies = dependencies
        configFilePath = os.path.expanduser('~/scrolls.conf')
        methods = ['useCommandlineArgs', 'selectApplications']
        if os.path.isfile(configFilePath):
            keys = [k for k in dir(self) if k[0] != '_' and k not in methods]
            defaults = {k: getattr(self, k) for k in keys}
            types = {k: type(defaults[k]) for k in keys}
            parser = configparser.ConfigParser()
            parser.read(configFilePath)
            if 'scrolls' not in parser.sections():
                raise ValueError('scrolls.conf requires a [scrolls] section.')
            for key in keys:
                if not parser.has_option('scrolls', key):
                    val = defaults[key]
                elif types[key] is str:
                    val = parser.get('scrolls', key)
                elif types[key] is bool:
                    val = parser.getboolean('scrolls', key)
                elif types[key] is list:
                    items = parser.get('scrolls', key).split(',')
                    val = [i.strip() for i in items if i is not '']
                setattr(self, key, val)

    def useCommandlineArgs(self, args):
        if hasattr(args, 'server'):
            self.server = args.server
        if hasattr(args, 'dry_run'):
            self.dry_run = args.dry_run

    def selectApplications(self):
        """Determine which programs to record log events for."""
        filesystem = self._dependencies.getFilesystem()
        log = self._dependencies.getLog()
        applications = {}
        packages = {
            'mongodb': {'mongodb': '/var/log/mongodb/mongodb.log'},
            'nginx': {
                'nginx-access': '/var/log/nginx/access.log',
                'nginx-error': '/var/log/nginx/error.log'
            },
        }
        for pkgName, pkgApplications in packages.items():
            if filesystem.hasPackage(pkgName):

                applications.update(pkgApplications)
                for name, logfile in pkgApplications.items():
                    log.selectedApplication(name=name, logfile=logfile)
        return applications
