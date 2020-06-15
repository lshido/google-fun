import unittest

from google_fun.code_solution import solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([1, 2, 3, 4], 15), [-1, -1])

    def test_2(self):
        self.assertEqual(solution([4, 3, 10, 2, 8], 12), [2, 3])