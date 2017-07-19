from test.ditestcase import DITestCase
from mock import patch


class CounterFactoryTests(DITestCase):

    def test_Single_attribute(self):
        from scrolls.factories.counter import CounterFactory
        count = CounterFactory(self.dependencies)
        with patch('scrolls.factories.counter.Counter') as Counter:
            counter = count.byApp()
            Counter.assert_called_with('app')
            self.assertEqual(counter, Counter())
            counter = count.byHostname()
            Counter.assert_called_with('hostname')
            self.assertEqual(counter, Counter())
