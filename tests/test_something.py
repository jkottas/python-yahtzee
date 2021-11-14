import unittest

class test_something(unittest.TestCase):
    def testAThing(self):
        self.assertEqual(2, 2)

    @unittest.skip("reason")
    def testAnotherThing(self):
        self.assertEqual(2, 3)