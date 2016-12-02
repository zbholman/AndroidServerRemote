import unittest
from md5hash import md5hash

class md5HashTestCase(unittest.TestCase):
        def test_md5Hash(self):
                self.assertTrue(md5hash())

if __name__=='__main__':
        unittest.main()
