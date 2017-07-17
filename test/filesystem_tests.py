from test.ditestcase import DITestCase
from mock import patch


class FilesystemTests(DITestCase):

    def test_hasPackage_Returns_false_if_aptcache_error(self):
        from scrolls.filesystem import Filesystem
        from subprocess import CalledProcessError
        with patch('scrolls.filesystem.subprocess') as subprocess:
            subprocess.CalledProcessError = CalledProcessError
            subprocess.check_output.side_effect = CalledProcessError(100, '?')
            filesys = Filesystem(self.dependencies)
            self.assertFalse(filesys.hasPackage('python-scrolls'))

    def test_hasPackage_Returns_true_if_package_found(self):
        from scrolls.filesystem import Filesystem
        with patch('scrolls.filesystem.subprocess') as subprocess:
            subprocess.check_output.return_value = ''
            filesys = Filesystem(self.dependencies)
            self.assertTrue(filesys.hasPackage('you-got-me'))
            self.log.foundPackage.assert_called_with('you-got-me')

    def test_write_notifies_log(self):
        from scrolls.filesystem import Filesystem
        with patch('scrolls.filesystem.open', create=True):
            filesys = Filesystem(self.dependencies)
            filesys.write('/my/file', 'my content')
            self.log.wroteFile.assert_called_with('/my/file',
                                                  'my content',
                                                  self.config.dry_run)

    def test_write_honors_dry_run(self):
        from scrolls.filesystem import Filesystem
        self.config.dry_run = True
        with patch('scrolls.filesystem.open', create=True) as open:
            filesys = Filesystem(self.dependencies)
            filesys.write('/my/file', 'my content')
            assert not open.called

    def test_run_honors_dry_run(self):
        from scrolls.filesystem import Filesystem
        self.config.dry_run = True
        with patch('scrolls.filesystem.subprocess') as subprocess:
            filesys = Filesystem(self.dependencies)
            filesys.run(['a', 'b', 'c'])
            assert not subprocess.check_call.called

    def test_run_notifies_log(self):
        from scrolls.filesystem import Filesystem
        with patch('scrolls.filesystem.subprocess') as subprocess:
            subprocess.check_output.return_value = ''
            filesys = Filesystem(self.dependencies)
            filesys.run(['a', 'b', 'c'])
            self.log.ranCommand.assert_called_with(['a', 'b', 'c'],
                                                   self.config.dry_run)
