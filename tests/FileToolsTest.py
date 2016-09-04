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

    def tearDown(self):
        os.remove(TEST_FILE)

if __name__ == "__main__":
    unittest.main()



