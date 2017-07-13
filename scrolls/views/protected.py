from pyramid.exceptions import HTTPForbidden


class ProtectedView(object):

    def __init__(self, request):
        self.request = request
        if not self.request.user_logged_in:
            raise HTTPForbidden()
