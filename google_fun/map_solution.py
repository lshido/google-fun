# Recursive functions should always try to solve the smallest possible problem.
# In this case, the problem is to get the next move if there is one.
# Before deciding the next move, we should decide if we need to move by checking to see
# if current is equal to goal. If it is, then it should get the length of the path + 1.
# Check to see if this path is shorter than the previously saved shortest path.
# Return the shorter path.
# For any position, there are theoretically four moves, up, down, left, right.
# The algo must take all of those that are valid paths. (it should not skip any valid moves)
# Check for validity of the move.
# If the row is less than the max row, and if the column is less than the max row
# If the row is more than 0, and the column is more than 0.
# If it's valid then that position should be added to the path.
# and current position should equal that move.
# Measure the length of path and save it.
# Then, feed current position back into the function.
# If there are no moves to make, then remove the current position from the path.
from copy import deepcopy
import pdb

def solution(map):
    all_paths = []
    for configuration in get_all_configurations(map):
        goal = (len(map) - 1, len(map[0]) - 1)
        valid_paths = get_valid_paths((0, 0), [], goal, configuration, [])
        all_paths.extend(valid_paths)
    if all_paths:
        min_length = min([len(path) for path in all_paths])
        if min_length > 0:
            return min_length + 1
        else:
            return None
    else:
        return None


def get_all_configurations(map):
    configurations = []
    original = deepcopy(map)
    configurations.append(original)
    max_row = len(original)
    max_column = len(original[0])
    for row in range(0, max_row):
        for column in range(0, max_column):
            A = deepcopy(original)
            if A[row][column] == 1:
                A[row][column] = 0
                configurations.append(A)
    return configurations


def get_valid_paths(current, past_moves, goal, map, valid_paths):
    row, column = current
    size = goal
    if current == goal:
        valid_path = deepcopy(past_moves)
        valid_paths.append(valid_path)
        return valid_paths

    up, down, left, right = ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1))
    
    past_moves.append(current)
    if is_valid(up, size) and not_wall(up, map) and not_visited(up, past_moves):
        valid_paths = get_valid_paths(up, past_moves, goal, map, valid_paths)

    if is_valid(down, size) and not_wall(down, map) and not_visited(down, past_moves):
        valid_paths = get_valid_paths(down, past_moves, goal, map, valid_paths)

    if is_valid(left, size) and not_wall(left, map) and not_visited(left, past_moves):
        valid_paths = get_valid_paths(left, past_moves, goal, map, valid_paths)

    if is_valid(right, size) and not_wall(right, map) and not_visited(right, past_moves):
        valid_paths = get_valid_paths(right, past_moves, goal, map, valid_paths)

    past_moves.remove(current)

    return valid_paths


def is_valid(move, size):
    valid = False
    row, column = move
    max_row, max_column = size
    if row >= 0 and column >= 0:
        if row <= max_row and column <= max_column:
            valid = True
    return valid

def not_wall(move, map):
    row, column = move
    if map[row][column] != 1:
        return True
    else:
        return False

def not_visited(move, past_moves):
    if not move in past_moves:
        return True
    else:
        return False