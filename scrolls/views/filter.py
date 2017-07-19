from pyramid.view import view_config, view_defaults
from scrolls.views.protected import ProtectedView


@view_defaults(context='scrolls.models.filter.Filter')
class FilterView(ProtectedView):

    def __init__(self, request):
        super(FilterView, self).__init__(request)

    @view_config(request_method='GET', renderer='filter.jinja2')
    def get(self):
        return {}
