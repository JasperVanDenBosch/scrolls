from pyramid import testing
from test.ditestcase import DITestCase


class ViewTestCase(DITestCase):

    def setUp(self):
        super(ViewTestCase, self).setUp()
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.user = None                 # By default no user logged in
        self.request.matchdict = {'iam': 'the matchdict'}
        self.request.POST = {'iam': 'the POST dict'}
        self.request.params = {'iam': 'the PARAMS dict'}
        self.request.dependencies = self.dependencies

    def tearDown(self):
        testing.tearDown()
