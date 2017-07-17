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
