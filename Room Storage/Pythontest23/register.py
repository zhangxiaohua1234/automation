import unittest


class MyTestCase(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, False)
    def test02(self):
        a=True
        self.assertTrue(a)


if __name__ == '__main__':
    unittest.main()
