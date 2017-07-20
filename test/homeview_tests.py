from test.viewtestcase import ViewTestCase


class HomeViewTests(ViewTestCase):

    def setUp(self):
        super(HomeViewTests, self).setUp()
        self.request.user_logged_in = True

    def test_get_returns_latest_messages(self):
        from scrolls.views.home import HomeView
        view = HomeView(self.request)
        out = view.get_latest()
        self.assertEqual(out['messages'], self.messages.getLatest())

    def test_get_returns_host_and_app_counts(self):
        from scrolls.views.home import HomeView
        view = HomeView(self.request)
        out = view.get_latest()
        self.assertEqual(out['hostnames'],
                         self.stats.get('hostname'))
        self.assertEqual(out['apps'],
                         self.stats.get('app'))

    def test_get_returns_filter(self):
        from scrolls.views.home import HomeView
        view = HomeView(self.request)
        out = view.get_latest()
        filter = self.request.context.getFilter()
        self.assertEqual(out['filter'], filter)
        self.messages.getLatest.assert_called_with(filter)
