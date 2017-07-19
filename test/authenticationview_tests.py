from test.viewtestcase import ViewTestCase
from mock import patch


class AuthenticationViewTests(ViewTestCase):

    def test_forbidden_view_redirects_to_login(self):
        from scrolls.views.authentication import AuthenticationView
        view = AuthenticationView(self.request)
        with self.assertRedirectsToContext('login'):
            view.get_forbidden()

    def test_get_login_redirects_to_home_if_already_logged_in(self):
        from scrolls.views.authentication import AuthenticationView
        view = AuthenticationView(self.request)
        self.request.user_logged_in = True
        with self.assertRedirectsToContext():
            view.get_login()

    def test_get_login_GET_return_empty(self):
        from scrolls.views.authentication import AuthenticationView
        view = AuthenticationView(self.request)
        self.request.method = 'GET'
        self.request.user_logged_in = False
        out = view.get_login()
        self.assertEqual(out, {'failedAttempt': False})

    def test_post_login_returns_message_if_password_nota_match(self):
        from scrolls.views.authentication import AuthenticationView
        self.request.user_logged_in = False
        self.request.POST['password'] = 'a guess'
        self.config.hashed_password = self.security.hashPassword('the truth')
        view = AuthenticationView(self.request)
        out = view.post_login()
        self.assertEqual(out, {'failedAttempt': True})

    def test_post_login_logs_in_if_password_matches(self):
        from scrolls.views.authentication import AuthenticationView
        self.request.user_logged_in = False
        self.request.POST['password'] = 'the truth'
        self.config.hashed_password = self.security.hashPassword('the truth')
        with patch('scrolls.views.authentication.remember') as remember:
            view = AuthenticationView(self.request)
            with self.assertRedirectsToContext() as redirect:
                view.post_login()
            remember.assert_called_with(self.request, 'user',
                                        max_age=str(60*60*24*7))
            redirect.assertIncludesHeaders(remember())

    def test_post_logout_forgets_you(self):
        from scrolls.views.authentication import AuthenticationView
        with patch('scrolls.views.authentication.forget') as forget:
            view = AuthenticationView(self.request)
            with self.assertRedirectsToContext('login') as redirect:
                view.post_logout()
            forget.assert_called_with(self.request)
            redirect.assertIncludesHeaders(forget())
