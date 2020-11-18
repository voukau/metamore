from metamore import __version__
import unittest


class TestVersion(unittest.TestCase):

    def test_version(self):
        self.assertEqual(__version__, '0.1.1')
