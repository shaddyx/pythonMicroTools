from microtools import FileTools
import unittest
import os
TEST_FILE="test.txt"
TEST_DATA="""This is a test data string
Multiline

"""

class FileToolsTest(unittest.TestCase):

    def test_putGetContents(self):
        FileTools.putContents(TEST_FILE, TEST_DATA)
        readed = FileTools.getContents(TEST_FILE)
        self.assertEqual(readed, TEST_DATA)

    def test_getDirContentsRec(self):
        res = FileTools.getDirContentsRec("./")
        self.assertTrue("./testFiles/test1" in res)
        self.assertTrue("./testFiles/test2" in res)
        res = FileTools.getDirContentsRec("./", "*2")
        self.assertFalse("./testFiles/test1" in res)
        self.assertTrue("./testFiles/test2" in res)

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

if __name__ == "__main__":
    unittest.main()
