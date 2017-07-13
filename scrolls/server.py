from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
import waitress


class Server(object):

    def __init__(self, dependencies):
        self.dependencies = dependencies

    def serve(self, config):
        wsgiapp = self.make_wsgi_app()
        waitress.serve(wsgiapp, host='0.0.0.0', port=80)

    def make_wsgi_app(self, **settings):
        settings['jinja2.directories'] = 'scrolls:templates'
        config = Configurator(settings=settings)
        authnPolicy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
        config.set_authentication_policy(authnPolicy)
        config.set_authorization_policy(ACLAuthorizationPolicy())
        config.include('pyramid_jinja2')
        config.add_route('home', '/')
        config.add_route('login', '/login')
        config.add_request_method(lambda r: self.dependencies,
                                  'dependencies', reify=True)
        config.add_request_method(lambda r: r.unauthenticated_userid,
                                  'user_logged_in', reify=True)
        config.scan('scrolls.views')
        return config.make_wsgi_app()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.

    This is a pyramid-style entrypoint to be used with e.g.:
        pserve development.ini
    """
    server = Server()
    return server.make_wsgi_app(**settings)
