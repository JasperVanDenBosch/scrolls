from test.viewtestcase import ViewTestCase
from pyramid.exceptions import HTTPForbidden


class ProtectedViewTests(ViewTestCase):

    def test_get_without_login_redirects_to_loginview(self):
        from scrolls.views.protected import ProtectedView
        self.config.hashed_password = 'a7b8b'
        with self.assertRaises(HTTPForbidden):
            ProtectedView(self.request)

    def test_get_without_login_when_no_password_set(self):
        from scrolls.views.protected import ProtectedView
        self.config.hashed_password = ''  # no password
        ProtectedView(self.request)  # no problem
