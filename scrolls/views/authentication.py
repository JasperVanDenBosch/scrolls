from pyramid.httpexceptions import HTTPFound
from pyramid.view import forbidden_view_config


class AuthenticationView(object):

    def __init__(self, request):
        self.request = request

    @forbidden_view_config()
    def get_forbidden(self):
        raise HTTPFound(self.request.route_url('login'))
