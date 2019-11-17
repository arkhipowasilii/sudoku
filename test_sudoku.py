from sudoku import get_dependent_indexes, main, solve_cell_sudoku, get_all_related_indexes
from typing import Set, List, Tuple
indexes_sudoku = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)],
                 [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)],
                 [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)],
                 [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)],
                 [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)],
                 [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)],
                 [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)],
                 [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)],
                 [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]]


def get_column_indexes(column_index: int) -> List[Tuple[int, int]]:
    result = []

    for row_index in range(9):
        result.append(indexes_sudoku[row_index][column_index])

    return result


def test_get_dependent_indexes():
    sudoku = [[0, 0, 0, 0, 6, 0, 7, 0, 0],
              [0, 5, 9, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 2, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [6, 0, 0, 5, 0, 0, 0, 0, 0],
              [3, 0, 0, 0, 0, 0, 4, 6, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 1],
              [8, 0, 0, 7, 4, 0, 0, 0, 0]]

    sudoku_cells = main(sudoku)

    sudoku_cells[0][0].use(2)
    sudoku_cells[0][1].use(4)
    dependent_indexes = get_dependent_indexes(sudoku_cells, 2, 1, 8)

    assert dependent_indexes == {(1, 6), (1, 7), (3, 8), (4, 8), (5, 8), (6, 8), (8, 8)}

    sudoku_cells[4][1].use(2)
    dependent_indexes = get_dependent_indexes(sudoku_cells, 2, 7, 2)
    assert dependent_indexes == {(8, 2), (6, 2), (7, 6), (7, 5), (7, 4)}


def test_solve_sudoku():
    sudoku = [[1, 0, 0, 0, 3, 0, 0, 0, 8],
              [0, 3, 0, 8, 0, 2, 0, 4, 0],
              [0, 0, 7, 0, 0, 0, 5, 0, 0],
              [0, 4, 0, 6, 0, 8, 0, 5, 0],
              [5, 0, 0, 0, 9, 0, 0, 0, 6],
              [0, 9, 0, 5, 0, 3, 0, 7, 0],
              [0, 0, 4, 0, 0, 0, 2, 0, 0],
              [0, 5, 0, 2, 0, 1, 0, 9, 0],
              [9, 0, 0, 0, 4, 0, 0, 0, 7]]


def test_get_all_related_indexes():

    all_related_indexes = get_all_related_indexes(0, 0)
    check = set(indexes_sudoku[0]
                 + get_column_indexes(0)
                 + [(1, 1), (1, 2), (2, 1), (2, 2)])
    check.remove((0, 0))
    assert check == all_related_indexes

    all_related_indexes = get_all_related_indexes(8, 8)
    check = set(indexes_sudoku[8]
                + get_column_indexes(8)
                + [(6, 6), (6, 7), (7, 6), (7, 7)])
    check.remove((8, 8))
    assert check == all_related_indexes

    all_related_indexes = get_all_related_indexes(4, 4)
    check = set(indexes_sudoku[4]
                + get_column_indexes(4)
                + [(3, 3), (3, 5), (5, 3), (5, 5)])
    check.remove((4, 4))
    assert check == all_related_indexes

    all_related_indexes = get_all_related_indexes(7, 4)
    check = set(indexes_sudoku[7]
                + get_column_indexes(4)
                + [(6, 3), (6, 5), (8, 3), (8, 5)])
    check.remove((7, 4))
    assert check == all_related_indexes


if __name__ == '__main__':
    test_get_dependent_indexes()
    test_solve_sudoku()
    test_get_all_related_indexes()

