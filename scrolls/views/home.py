from pyramid.view import view_config, view_defaults
from scrolls.views.protected import ProtectedView


@view_defaults(route_name='home')
class HomeView(ProtectedView):

    def __init__(self, request):
        super(HomeView, self).__init__(request)
        self.messages = request.dependencies.getMessageRepository()

    @view_config(request_method='GET', renderer='home.jinja2')
    def get(self):
        return {'latest': self.messages.getLatest()}
