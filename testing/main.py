'''class TestCuboid(unittest.TestCase):
    test = set()
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),0)
        self.assertIs(addSet(test, "test"))

    def test_input_value(self):
        self.assertRaises(TypeError, cuboid_volume, True)'''


from cuboid_volume import add,size,checkElements,delete
import unittest

class TestSet(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add("asu"), True)
        self.assertEqual(size(), 1)
        self.assertEqual(checkElements("asu"), ["asu"])
        self.assertEqual(add("asu"), False)
        self.assertEqual(checkElements("asu"), ["asu"])
    def remove(self):
        self.assertEqual(delete("asu"), True)
        self.assertEqual(checkElements("asu"),[])
        self.assertEqual(size(), 0)

if __name__ == '__main__':
    unittest.main()
