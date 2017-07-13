from pyramid import testing
from test.ditestcase import DITestCase
from test.redirectioncontextmanager import RedirectionContextManager


class ViewTestCase(DITestCase):

    def setUp(self):
        super(ViewTestCase, self).setUp()
        self.pyramidconfig = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.user_logged_in = False

        def route_url(route, **kwargs):
            return route, kwargs
        self.request.route_url = route_url
        self.request.matchdict = {'iam': 'the matchdict'}
        self.request.POST = {'iam': 'the POST dict'}
        self.request.params = {'iam': 'the PARAMS dict'}
        self.request.dependencies = self.dependencies

    def tearDown(self):
        testing.tearDown()

    def assertRedirectsTo(self, route, **kwargs):
        loc = self.request.route_url(route, **kwargs)
        return RedirectionContextManager(self, loc)
