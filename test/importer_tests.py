from test.ditestcase import DITestCase
from mock import sentinel, Mock


class ImporterTests(DITestCase):

    def test_If_no_messages_doesnt_do_anything(self):
        from scrolls.importer import MessageImporter
        importer = MessageImporter(self.dependencies)
        importer.import_([])
        assert not self.messages.add.called

    def test_Tells_repo_to_persist_messages(self):
        from scrolls.importer import MessageImporter
        importer = MessageImporter(self.dependencies)
        importer.import_([sentinel.m1, sentinel.m2])
        self.messages.add.assert_called_with([sentinel.m1, sentinel.m2])

    def test_Runs_each_message_through_each_counter_then_updates_repo(self):
        from scrolls.importer import MessageImporter
        importer = MessageImporter(self.dependencies)
        counter1, counter2 = Mock(), Mock()
        importer.counters = [counter1, counter2]
        importer.import_([sentinel.m1, sentinel.m2])
        counter1.add.assert_any_call(sentinel.m1)
        counter1.add.assert_any_call(sentinel.m2)
        counter2.add.assert_any_call(sentinel.m1)
        counter2.add.assert_any_call(sentinel.m2)
        self.stats.update.assert_any_call(counter1.name, counter1.counts)
        self.stats.update.assert_any_call(counter2.name, counter2.counts)
        counter1.reset.assert_called_with()
        counter2.reset.assert_called_with()

    def test_has_counter_byApp(self):
        from scrolls.importer import MessageImporter
        importer = MessageImporter(self.dependencies)
        self.assertIn(self.count.byApp(), importer.counters)

    def test_has_counter_byHostname(self):
        from scrolls.importer import MessageImporter
        importer = MessageImporter(self.dependencies)
        self.assertIn(self.count.byHostname(), importer.counters)
