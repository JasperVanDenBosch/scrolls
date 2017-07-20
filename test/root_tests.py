from test.ditestcase import DITestCase


class RootTests(DITestCase):

    def test_filter_returns_Filter(self):
        from scrolls.models.root import Root
        from scrolls.models.filter import Filter
        root = Root(None)
        self.assertIsInstance(root['filter'], Filter)

    def test_getFilter_returns_Filter(self):
        from scrolls.models.root import Root
        from scrolls.models.filter import Filter
        root = Root(None)
        self.assertIsInstance(root.getFilter(), Filter)
