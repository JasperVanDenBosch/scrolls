from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
import waitress
import operator


class Server(object):

    def __init__(self, dependencies):
        self.dependencies = dependencies
        self.config = self.dependencies.getConfiguration()

    def serve(self, config):
        wsgiapp = self.make_wsgi_app()
        waitress.serve(wsgiapp, host='0.0.0.0', port=80)

    def make_wsgi_app(self, **settings):
        settings['jinja2.directories'] = 'scrolls:templates'
        pyrConf = Configurator(settings=settings)
        secret = self.config.ticket_secret
        authnPolicy = AuthTktAuthenticationPolicy(secret, hashalg='sha512')
        pyrConf.set_authentication_policy(authnPolicy)
        pyrConf.set_authorization_policy(ACLAuthorizationPolicy())
        pyrConf.include('pyramid_jinja2')

        def setup_jinja2_env():
            def sortedStats(stat):
                return sorted(stat.items(), key=operator.itemgetter(1),
                              reverse=True)

            env = pyrConf.get_jinja2_environment()
            env.filters['sortedStats'] = sortedStats
        pyrConf.action(None, setup_jinja2_env, order=999)

        pyrConf.add_static_view('static', 'static', cache_max_age=10)
        pyrConf.add_route('home', '/')
        pyrConf.add_route('login', '/login')
        pyrConf.add_route('logout', '/logout')
        pyrConf.add_request_method(lambda r: self.dependencies,
                                   'dependencies', reify=True)
        pyrConf.add_request_method(lambda r: r.unauthenticated_userid,
                                   'user_logged_in', reify=True)
        pyrConf.scan('scrolls.views')
        return pyrConf.make_wsgi_app()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.

    This is a pyramid-style entrypoint to be used with e.g.:
        pserve development.ini
    """
    server = Server()
    return server.make_wsgi_app(**settings)
