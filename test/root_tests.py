from test.ditestcase import DITestCase
from mock import Mock


class RootTests(DITestCase):

    def setUp(self):
        super(RootTests, self).setUp()
        self.request = Mock()
        self.request.dependencies = self.dependencies

    def test_filter_returns_Filter(self):
        from scrolls.models.root import Root
        from scrolls.models.filter import Filter
        root = Root(self.request)
        self.assertIsInstance(root['filter'], Filter)

    def test_getFilter_returns_Filter(self):
        from scrolls.models.root import Root
        from scrolls.models.filter import Filter
        root = Root(self.request)
        self.assertIsInstance(root.getFilter(), Filter)

    def test_getIdResolver_returns_IdResolver(self):
        from scrolls.models.root import Root
        from scrolls.idresolver import IdResolver
        root = Root(self.request)
        self.assertIsInstance(root.getIdResolver(), IdResolver)
        self.assertIsInstance(root['id'], IdResolver)
