from test.viewtestcase import ViewTestCase


class AuthenticationViewTests(ViewTestCase):

    def test_forbidden_view_redirects_to_login(self):
        from scrolls.views.authentication import AuthenticationView
        view = AuthenticationView(self.request)
        with self.assertRedirectsTo('login'):
            view.get_forbidden()