from test.ditestcase import DITestCase
from mock import Mock


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

    def messageToDict(self, d):
        message = Mock()
        message.toDict.return_value = d
        return message
