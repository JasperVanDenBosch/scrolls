from test.viewtestcase import ViewTestCase


class HomeViewTests(ViewTestCase):

    def test_get_returns_study_and_experiment(self):
        from scrolls.views.home import HomeView
        view = HomeView(self.request)
        out = view.get()
        self.assertEqual(out['latest'], self.messages.getLatest())
