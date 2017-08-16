import unittest

def simpleFunction(x):
  return x + 1

class SimpleFunctionTest(unittest.TestCase):

  def setUp(self):
    print("This is run before all of our tests have a chance to execute")

  def tearDown(self):
    print("This is executed after all of our tests have completed")

  def test_simple_function(self):
    print("Testing that our function works with positive tests")
    self.assertEqual(simpleFunction(2), 3)
    self.assertEqual(simpleFunction(234135145145432143214321432), 234135145145432143214321433)
    self.assertEqual(simpleFunction(0), 1)
  
  def test_negative_simple_function(self):
    self.assertNotEqual(simpleFunction(2), 4)


if __name__ == '__main__':
  unittest.main()