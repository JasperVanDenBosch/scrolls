from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.view import view_config, view_defaults
from pyramid.security import remember, forget


@view_defaults(context='scrolls.models.root.Root', renderer='login.jinja2')
class AuthenticationView(object):

    def __init__(self, request):
        self.request = request
        self.security = self.request.dependencies.getSecurity()
        self.config = self.request.dependencies.getConfiguration()

    @view_config(context=HTTPForbidden)
    def get_forbidden(self):
        login_url = self.request.resource_url(self.request.root, 'login')
        return HTTPFound(login_url)

    @view_config(name='login', request_method='GET')
    def get_login(self):
        if self.request.user_logged_in:
            raise HTTPFound(self.context_url())
        return {'failedAttempt': False}

    @view_config(name='login', request_method='POST')
    def post_login(self):
        self.get_login()
        password = self.request.POST.get('password')
        hashed = self.security.hashPassword(password)
        if hashed == self.config.hashed_password:
            headers = remember(self.request, 'user', max_age=str(60*60*24*7))
            raise HTTPFound(self.context_url(), headers=headers)
        return {'failedAttempt': True}

    @view_config(name='logout', request_method='POST')
    def post_logout(self):
        headers = forget(self.request)
        raise HTTPFound(self.context_url('login'), headers=headers)

    def context_url(self, *elements, **kw):
        return self.request.resource_url(self.request.context, *elements, **kw)
