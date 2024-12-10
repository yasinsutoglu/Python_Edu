import unittest
import main2

class TestGame(unittest.TestCase):
    def test_input(self):
        # please note in the video, I had the parameters flipped it should be the "guess" parameter 1st and "answer" parameter 2nd
        result = main2.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main2.run_guess(0, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = main2.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main2.run_guess(int('11'), 5)
        self.assertFalse(isinstance(result, TypeError))


if __name__ == '__main__':
    unittest.main()