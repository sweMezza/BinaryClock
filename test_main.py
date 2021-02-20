import unittest
import main

class TestBinaryClock(unittest.TestCase):
    #convertinttobinlist

    def test_default(self):
        in_value = "Verify"
        result = in_value

        self.assertEqual(result, in_value)

    def test_0(self):
        in_value = 0
        result = main.convertinttobinlist(in_value)
        self.assertEqual(result, [0])

    def test_0_4long(self):
        in_value = 0
        result = main.convertinttobinlist(in_value, 4)
        self.assertEqual(result, [0, 0, 0, 0])

    def test_1(self):
        in_value = 1
        result = main.convertinttobinlist(in_value)
        self.assertEqual(result, [1])

    def test_2(self):
        in_value = 2
        result = main.convertinttobinlist(in_value)
        self.assertEqual(result, [1, 0])

    def test_2_4long(self):
        in_value = 2
        result = main.convertinttobinlist(in_value, 4)
        self.assertEqual(result, [0, 0, 1, 0])

    def test_24(self):
        in_value = 24
        result = main.convertinttobinlist(in_value)
        self.assertEqual(result, [1, 1, 0, 0, 0])

    def test_255(self):
        in_value = 255
        result = main.convertinttobinlist(in_value)
        self.assertEqual(result, [1, 1, 1, 1, 1, 1, 1, 1])

if __name__ == "__main__":
    unittest.main()