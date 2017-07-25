from test.ditestcase import DITestCase
from mock import Mock
from datetime import datetime


class CounterFactoryTests(DITestCase):

    def test_Name(self):
        from scrolls.models.counter import Counter
        count = Counter('blub')
        self.assertEqual(count.name, 'blub')
        self.assertEqual(count.counts, {})

    def test_Counting_and_reset(self):
        from scrolls.models.counter import Counter
        count = Counter('blub')
        self.assertEqual(count.counts, {})
        count.add(self.messageToDict({'blub': 'a'}))
        count.add(self.messageToDict({'blub': 'b'}))
        count.add(self.messageToDict({'blub': 'a'}))
        self.assertEqual(count.counts, {
            ('blub', 'a'): 2,
            ('blub', 'b'): 1,
        })
        count.add(self.messageToDict({'blub': 'c'}))
        count.add(self.messageToDict({'blub': 'b'}))
        self.assertEqual(count.counts, {
            ('blub', 'a'): 2,
            ('blub', 'b'): 2,
            ('blub', 'c'): 1,
        })
        count.reset()
        self.assertEqual(count.counts, {})

    def test_Count_by_time_bin(self):
        from scrolls.models.counter import Counter
        count = Counter('blub', '%a %d %b')
        self.assertEqual(count.counts, {})
        count.add(self.messageToDict({'datetime': datetime(2017, 7, 4, 11)}))
        count.add(self.messageToDict({'datetime': datetime(2017, 7, 5, 12)}))
        count.add(self.messageToDict({'datetime': datetime(2017, 7, 4, 13)}))
        self.assertEqual(count.counts, {
            ('blub', 'Tue 04 Jul'): 2,
            ('blub', 'Wed 05 Jul'): 1,
        })

    def test_If_attr_value_not_available_dont_count(self):
        from scrolls.models.counter import Counter
        count = Counter('blub')
        self.assertEqual(count.counts, {})
        count.add(self.messageToDict({'a': '2'}))
        count.add(self.messageToDict({'blub': '1'}))
        self.assertEqual(count.counts, {
            ('blub', '1'): 1,
        })

    def messageToDict(self, d):
        message = Mock()
        message.toDict.return_value = d
        return message
