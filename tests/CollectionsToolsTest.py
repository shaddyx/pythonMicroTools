import unittest

from microtools import ClassTools
from microtools.CollectionsTools import getPath

d = {
    "a":[
        {
            "b": 2
        }
    ]
}

class CollectionToolsTest(unittest.TestCase):
    def test_getOk(self):
        self.assertEqual(2, getPath(d, "a", 0, "b"))
    def test_getOk(self):
        self.assertEqual(None, getPath(d, "a", 0, "v"))
        self.assertEqual(None, getPath(d, "a", 1, "b"))
        self.assertEqual(None, getPath(d, "b", 1, "v"))

if __name__ == "__main__":
    unittest.main()
