import unittest

from google_fun.message_solution import solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([3, 1, 4, 1]), 4311)

    def test_2(self):
        self.assertEqual(solution([3, 1, 4, 1, 5, 9]), 94311)