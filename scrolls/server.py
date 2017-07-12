from pyramid.config import Configurator
import waitress


class Server(object):

    def __init__(self, dependencies):
        self.dependencies = dependencies

    def serve(self, config):
        wsgiapp = self.make_wsgi_app()
        waitress.serve(wsgiapp, host='0.0.0.0', port=6543)

    def make_wsgi_app(self, **settings):
        settings['jinja2.directories'] = 'scrolls:templates'
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.add_route('home', '/')
        config.add_request_method(lambda r: self.dependencies, 'dependencies',
                                  reify=True)
        config.scan('scrolls.views')
        return config.make_wsgi_app()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.

    This is a pyramid-style entrypoint to be used with e.g.:
        pserve development.ini
    """
    server = Server()
    return server.make_wsgi_app(**settings)
