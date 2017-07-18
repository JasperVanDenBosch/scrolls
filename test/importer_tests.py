from test.ditestcase import DITestCase
from mock import sentinel


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
