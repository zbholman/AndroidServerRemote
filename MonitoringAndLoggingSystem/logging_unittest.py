import unittest
import json
from logging import Log

# assertEquals(a, b, msg=None) a == b
# assertNotEqual(a, b, msg=None) a != b
# assertTrue(x) bool(x) is True
# assertFalse(x) bool(x) is False
# assertIs(a, b) a is b
# assertIsNot(a, b) a is not b
# assertIsNone(x) x is None
# assertIsNotNone(x) x is not None
# assertIn(a, b) a in b
# assertNotIn(a, b) a not in b
# assertIsInstance(a, b) isinstance(a, b)
# assertNotIsInstance(a, b) not isinstance(a, b)
# assertRaises

class MyTest(unittest.TestCase):
    def setUp(self):
        pass
  
    def testInc_Message(self):
        self.assertEqual(inc_Message.Return_Payload(),"HC")
        
if __name__ == '__main__':
    unittest.main()
