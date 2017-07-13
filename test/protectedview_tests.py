from test.viewtestcase import ViewTestCase
from pyramid.exceptions import HTTPForbidden


class ProtectedViewTests(ViewTestCase):

    def test_get_without_login_redirects_to_loginview(self):
        from scrolls.views.protected import ProtectedView
        with self.assertRaises(HTTPForbidden):
            ProtectedView(self.request)