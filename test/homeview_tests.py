from test.viewtestcase import ViewTestCase


class HomeViewTests(ViewTestCase):

    def setUp(self):
        super(HomeViewTests, self).setUp()
        self.request.user_logged_in = True

    def test_get_returns_latest_messages(self):
        from scrolls.views.home import HomeView
        view = HomeView(self.request)
        out = view.get()
        self.assertEqual(out['latest'], self.messages.getLatest())

    def test_get_returns_host_and_app_counts(self):
        from scrolls.views.home import HomeView
        view = HomeView(self.request)
        out = view.get()
        self.assertEqual(out['hostnames'],
                         self.stats.get('hostname'))
        self.assertEqual(out['apps'],
                         self.stats.get('app'))
