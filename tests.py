# -*- coding: utf-8 -*-

import unittest


class BasicTestsCase(unittest.TestCase):

    def test_1(self):

        self.assertTrue(10.5 > 10)
        self.assertTrue(11 > 10.5)
        self.assertTrue(11 > 10)
        self.assertEqual(11, 10 + 1)
        self.assertEqual(12, 10 + 2)

    def test_2(self):
        self.assertIn(1, [1, 2, 3])
        self.assertIn(2, [2, 1, 1])
        self.assertNotIn(2, [3, 4, 5])


class LinuxCommandsTestsCase(unittest.TestCase):

    def test_1(self):
        commands = ['ls', 'cd', 'mkdir', 'file']

        self.assertIn('ls', commands)
        self.assertIn('cd', commands)
        self.assertIn('mkdir', commands)

    def _num_to_perm(self, num):
        # Don't touch this method
        d = {'7':'rwx', '6': 'rw-', '5': 'r-x', '4': 'r--', '0': '---'}
        return ''.join(d.get(x, '') for x in num)

    def test_2(self):
        c = self._num_to_perm('777')
        self.assertEqual(c, 'rwxrwxrwx')
        c = self._num_to_perm('775')
        self.assertEqual(c, 'rwxrwxr-x')
        c = self._num_to_perm('644')
        self.assertEqual(c, 'rw-r--r--')

    def test_3(self):
        c = self._num_to_perm('400')
        self.assertEqual(c, 'r--------')
        c = self._num_to_perm('555')
        self.assertEqual(c, 'r-xr-xr-x')
        c = self._num_to_perm('744')
        self.assertEqual(c, 'rwxr--r--')

unittest.main()
