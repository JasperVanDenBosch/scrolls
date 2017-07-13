from test.viewtestcase import ViewTestCase
from mock import patch


class AuthenticationViewTests(ViewTestCase):

    def test_forbidden_view_redirects_to_login(self):
        from scrolls.views.authentication import AuthenticationView
        view = AuthenticationView(self.request)
        with self.assertRedirectsTo('login'):
            view.get_forbidden()

    def test_getOrPost_login_redirects_to_home_if_already_logged_in(self):
        from scrolls.views.authentication import AuthenticationView
        view = AuthenticationView(self.request)
        self.request.user_logged_in = True
        with self.assertRedirectsTo('home'):
            view.getOrPost_login()

    def test_getOrPost_login_GET_return_empty(self):
        from scrolls.views.authentication import AuthenticationView
        view = AuthenticationView(self.request)
        self.request.method = 'GET'
        self.request.user_logged_in = False
        out = view.getOrPost_login()
        self.assertEqual(out, {})

    def test_getOrPost_login_POST_logs_in(self):
        from scrolls.views.authentication import AuthenticationView
        self.request.method = 'POST'
        self.request.user_logged_in = False
        with patch('scrolls.views.authentication.remember') as remember:
            view = AuthenticationView(self.request)
            with self.assertRedirectsTo('home') as redirect:
                view.getOrPost_login()
            remember.assert_called_with(self.request, 'user',
                                        max_age=str(60*60*24*7))
            redirect.assertIncludesHeaders(remember())


