import unittest

from google_fun.cake_solution import solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution("abcabcabc"), 3)

    def test_2(self):
        self.assertEqual(solution("abcddbcaabcddbca"), 2)