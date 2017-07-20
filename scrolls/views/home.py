from pyramid.view import view_config, view_defaults
from scrolls.views.protected import ProtectedView


@view_defaults(request_method='GET', renderer='messages.jinja2')
class HomeView(ProtectedView):

    def __init__(self, request):
        super(HomeView, self).__init__(request)
        self.messages = request.dependencies.getMessageRepository()
        self.stats = request.dependencies.getStatisticRepository()
        self.count = request.dependencies.getCounterFactory()

    @view_config(context='scrolls.models.filter.Filter')
    @view_config(context='scrolls.models.root.Root')
    def get_latest(self):
        filter = self.request.context.getFilter()
        return {
            'messages': self.messages.getLatest(filter),
            'filter': filter,
            'hostnames': self.stats.get('hostname'),
            'apps': self.stats.get('app')
        }
