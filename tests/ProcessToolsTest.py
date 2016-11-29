from microtools import ProcessTools
import unittest

class ProcessToolsTest(unittest.TestCase):
    def test_execute(self):
        res = ProcessTools.execute(["echo","qwerqwerqwer"])
        print (str(res))

    def test_executeAsync(self):
        res = ProcessTools.execute(["echo", "1234"], wait=False)
        self.assertEqual("1234\n", res.readLine())
        self.assertEqual(None, res.readLine())

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
