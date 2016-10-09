import unittest

from microtools.DI import Service, Locator


@Service()
class Dependency1(object):
    pass
@Service()
class Dependency2(object):
    pass

class FileToolsTest(unittest.TestCase):

    def test_LocatorGetInstance(self):
        dep1 = Locator.getInstance(Dependency1)
        dep1_n = Locator.getInstance(Dependency1)
        self.assertEqual(dep1, dep1_n)

    def test_LocatorGetInstance(self):
        dep1 = Locator.getInstance(Dependency1)
        dep1_n = Locator.getInstance(Dependency2)
        self.assertNotEqual(dep1, dep1_n)




if __name__ == "__main__":
    unittest.main()
