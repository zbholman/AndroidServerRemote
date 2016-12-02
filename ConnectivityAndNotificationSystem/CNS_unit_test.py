import unittest
from CNS import msgQueue
from CNS import sendToNotification

class CNSTestCase(unittest.TestCase):

  def test_msgQueue(self):
    self.assertTrue(msgQueue())
    
  def test_sendToNotification(self):
    self.assertTrue(sendToNotifiation('CNS'))
    
if __name__ == '__main__':
  unittest.main()
