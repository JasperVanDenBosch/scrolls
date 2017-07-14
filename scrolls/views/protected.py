from pyramid.exceptions import HTTPForbidden


class ProtectedView(object):

    def __init__(self, request):
        self.request = request
        self.config = self.request.dependencies.getConfiguration()
        if self.config.hashed_password and not self.request.user_logged_in:
            raise HTTPForbidden()
