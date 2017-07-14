from pyramid.httpexceptions import HTTPFound
from pyramid.view import forbidden_view_config, view_config, view_defaults
from pyramid.security import remember, forget


@view_defaults(renderer='login.jinja2')
class AuthenticationView(object):

    def __init__(self, request):
        self.request = request
        self.security = self.request.dependencies.getSecurity()
        self.config = self.request.dependencies.getConfiguration()

    @forbidden_view_config()
    def get_forbidden(self):
        raise HTTPFound(self.request.route_url('login'))

    @view_config(route_name='login', request_method='GET')
    def get_login(self):
        if self.request.user_logged_in:
            raise HTTPFound(self.request.route_url('home'))
        return {'failedAttempt': False}

    @view_config(route_name='login', request_method='POST')
    def post_login(self):
        self.get_login()
        password = self.request.POST.get('password')
        hashed = self.security.hashPassword(password)
        if hashed == self.config.hashed_password:
            headers = remember(self.request, 'user', max_age=str(60*60*24*7))
            raise HTTPFound(self.request.route_url('home'), headers=headers)
        return {'failedAttempt': True}

    @view_config(route_name='logout', request_method='POST')
    def post_logout(self):
        headers = forget(self.request)
        raise HTTPFound(self.request.route_url('login'), headers=headers)
