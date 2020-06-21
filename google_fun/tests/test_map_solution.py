# test cases for:
# single move deadend
# two move deadends
# step move deadends
# two dead ends
import unittest

from map_solution_2 import get_valid_paths, solution, get_all_configurations


class TestGetAllConfigurations(unittest.TestCase):

    def test_1(self):
        layout = [
            [0, 1, 1, 0],
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [1, 1, 1, 0]
        ]
        self.assertEqual(get_all_configurations(layout), [
            [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]
            ],
            [
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]
            ],
            [
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                [1, 1, 0, 0],
                [1, 1, 1, 0]
            ],
            [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [0, 1, 0, 0],
                [1, 1, 1, 0]
            ],
            [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0],
                [1, 1, 1, 0]
            ],
            [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [0, 1, 1, 0]
            ],
            [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 0, 1, 0]
            ],
            [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 0, 0]
            ]])

class TestGetValidPaths(unittest.TestCase):

    def test_single_deadend(self):
        map = [
                [0, 1, 1],
                [0, 0, 1],
                [1, 1, 1],
            ]
        self.assertEqual(get_valid_paths((0, 0), [], (2, 2), map, []),
        [])

    def test_two_move_deadend(self):
        map = [
                [0, 1, 1],
                [0, 0, 0],
                [1, 1, 1],
            ]
        self.assertEqual(get_valid_paths((0, 0), [], (2, 2), map, []),
        [])

    def test_two_deadends(self):
        map = [
                [0, 1, 1],
                [0, 0, 0],
                [1, 0, 1],
            ]
        self.assertEqual(get_valid_paths((0, 0), [], (2, 2), map, []),
        [])

    def test_two_valid_paths(self):
        map = [
                [0, 1, 1],
                [0, 0, 0],
                [1, 0, 0],
            ]
        self.assertEqual(get_valid_paths((0, 0), [], (2, 2), map, []),
        [
            [(0, 0), (1, 0), (1, 1), (2, 1)],
            [(0, 0), (1, 0), (1, 1), (1, 2)]
        ])

    def test_two_valid_long_paths(self):
        map = [
                [0, 1, 1, 1],
                [0, 0, 0, 0],
                [1, 0, 1, 0],
                [1, 0, 0, 0],
            ]
        self.assertEqual(get_valid_paths((0, 0), [], (3, 3), map, []),
        [
            [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2)],
            [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)]
        ])

class TestSolution(unittest.TestCase):

    def test_single_deadend(self):
        self.assertEqual(solution(
            [
                [0, 1, 1],
                [0, 0, 1],
                [1, 1, 1],
            ]), None)

    def test_two_move_deadend(self):
        self.assertEqual(solution(
            [
                [0, 1, 1],
                [0, 0, 0],
                [1, 1, 1],
            ]), 5)

    def test_two_deadends(self):
        self.assertEqual(solution(
            [
                [0, 1, 1],
                [0, 0, 0],
                [1, 0, 1],
            ]), 5)

    def test_up_and_down(self):
        self.assertEqual(solution(
            [
                [0, 1, 0, 0, 0, 1],
                [0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1],
                [0, 0, 0, 1, 0, 0]
            ]), 11)

    def test_maze(self):
        self.assertEqual(solution(
            [
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1, 1],
                [1, 1, 1, 0, 0, 0]
            ]), 11)

    def test_all_zero(self):
        self.assertEqual(solution(
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ]), 11)

    def test_1(self):
        self.assertEqual(solution(
            [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]
            ]), 7)

    def test_2(self):
        self.assertEqual(solution(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]
            ]), 11)

    def test_3(self):
        self.assertEqual(solution(
            [
                [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 1, 1, 0]
            ]), 18)