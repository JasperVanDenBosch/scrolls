from pyramid.view import view_config, view_defaults


@view_defaults(route_name='home')
class HomeView(object):

    def __init__(self, request):
        self.request = request
        self.messages = request.dependencies.getMessageRepository()

    @view_config(request_method='GET', renderer='home.jinja2')
    def get(self):
        return {'latest': self.messages.getLatest()}
