import unittest

from microtools import ClassTools
class TestClass:
    a=1
    b=2
    c=3

class ClassToolsTest(unittest.TestCase):
    def test_getVars(self):
        d=ClassTools.getVars(TestClass())
        self.assertEqual(d["a"], TestClass.a)
        self.assertEqual(d["b"], TestClass.b)
        self.assertEqual(d["c"], TestClass.c)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
