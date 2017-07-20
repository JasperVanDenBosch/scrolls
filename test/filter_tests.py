from test.ditestcase import DITestCase
from mock import Mock


class FilterTests(DITestCase):

    def test_getFilter_returns_self(self):
        from scrolls.models.filter import Filter
        root = Mock()
        filter = Filter(root)
        self.assertEqual(filter.getFilter(), filter)

    def test_getFilter_traversal(self):
        from scrolls.models.filter import Filter
        root = Mock()
        rootFilter = Filter(root)
        self.assertEqual(rootFilter.__name__, 'filter')
        self.assertEqual(rootFilter.__parent__, root)
        self.assertFalse(rootFilter.resolvable)
        self.assertEqual(rootFilter.path, ())
        with self.assertRaises(KeyError):
            rootFilter['bla']
        appFilter = rootFilter['app']
        self.assertEqual(appFilter.__name__, 'app')
        self.assertEqual(appFilter.__parent__, rootFilter)
        self.assertFalse(appFilter.resolvable)
        self.assertEqual(appFilter.path, ('app',))
        nginx2Filter = appFilter['nginx2']
        self.assertEqual(nginx2Filter.__name__, 'nginx2')
        self.assertEqual(nginx2Filter.__parent__, appFilter)
        self.assertTrue(nginx2Filter.resolvable)
        self.assertEqual(nginx2Filter.path, ('app','nginx2'))
        with self.assertRaises(KeyError):
            nginx2Filter['bla2']
