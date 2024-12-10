# If you have 10 pyfile or modules, so you should have 10 test file for each of them.
# Test file is a .py file also.
# All the test_function names should be unique in class.

# Alternative Test-Run:
# Console Command: python3 -m unittest -v

# BASIC PRECAUTIONS Below:
# pylint
# pyflakes => another linter
# AutoPEP 8

# --------------------------------------
import unittest
import main
class TestMain(unittest.TestCase):  # inheriting TestCase class
	def setUp(self):  # this method will run before starting all the other test methods
		print("Starting a method/test: ")

	def test_add(self):
		'''This is the info for this particular test'''
		test_param = 10
		result = main.do_stuff(test_param)
		self.assertEqual(result, 15)

	def test_add2(self):
		test_param = 'random string'
		result = main.do_stuff(test_param)
		self.assertTrue(isinstance(result, ValueError))

	def tearDown(self):
		# this method will run after every test method. Generally used to reset/cleaning up data variables.
		print("Cleaning up....")


if __name__ == '__main__':
    unittest.main()