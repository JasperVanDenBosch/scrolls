from test.ditestcase import DITestCase
from mock import Mock


class FilterTests(DITestCase):

    def test_resource(self):
        from scrolls.models.filter import Filter
        root = Mock()
        filter = Filter(root)
        self.assertEqual(filter.__name__, 'filter')
        self.assertEqual(filter.__parent__, root)
