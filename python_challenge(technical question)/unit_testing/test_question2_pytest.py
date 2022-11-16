import Question_2
import unittest


class TestQuestion_2(unittest.TestCase):

    def test_exponent(self):
        self.assertEqual(Question_2.exponent(5, 5), 25)


if __name__ == '__main__':
    unittest.main()
