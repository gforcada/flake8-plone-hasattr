# -*- coding: utf-8 -*-
from flake8_plone_hasattr import PloneHasattrChecker
from tempfile import mkdtemp

import os
import mock
import unittest


class TestFlake8PloneAPI(unittest.TestCase):

    def _given_a_file_in_test_dir(self, contents):
        test_dir = os.path.realpath(mkdtemp())
        file_path = os.path.join(test_dir, 'test.py')
        with open(file_path, 'w') as a_file:
            a_file.write(contents)

        return file_path

    def test_no_hasattr_everything_is_fine(self):
        file_path = self._given_a_file_in_test_dir(
            'import os'
        )
        checker = PloneHasattrChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_hasattr(self):
        file_path = self._given_a_file_in_test_dir(
            'a = 3\n'
            '\n'
            '    hasattr(a, "max")\n'
        )
        checker = PloneHasattrChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 3)
        self.assertEqual(ret[0][1], 4)
        self.assertTrue(ret[0][2].startswith('P002 found '))

    @mock.patch('flake8_plone_hasattr.stdin_utils.stdin_get_value')
    def test_stdin(self, stdin_get_value):
        stdin_value = mock.Mock()
        stdin_value.splitlines.return_value = [
            'a = 3\n',
            '\n',
            '    hasattr(a, "max")\n',
        ]
        stdin_get_value.return_value = stdin_value

        checker = PloneHasattrChecker(None, 'stdin')
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 3)
        self.assertEqual(ret[0][1], 4)
        self.assertTrue(ret[0][2].startswith('P002 found '))


if __name__ == '__main__':
    unittest.main()
