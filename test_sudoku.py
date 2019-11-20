from sudoku import get_dependent_indexes, main, solve_cell_sudoku, get_all_related_indexes, exclude
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
    exclude(sudoku_cells, 2, 0, 0)
    sudoku_cells[0][1].use(3)
    exclude(sudoku_cells, 3, 0, 1)
    sudoku_cells[0][2].use(4)
    exclude(sudoku_cells, 4, 0, 2)
    sudoku_cells[0][3].use(8)
    exclude(sudoku_cells, 8, 0, 3)
    sudoku_cells[0][5].use(5)
    exclude(sudoku_cells, 5, 0, 5)
    sudoku_cells[0][7].use(1)
    exclude(sudoku_cells, 1, 0, 7)
    sudoku_cells[0][8].use(9)
    exclude(sudoku_cells, 9, 0, 8)
    sudoku_cells[1][0].use(7)
    exclude(sudoku_cells, 7, 1, 0)
    sudoku_cells[1][3].use(4)
    exclude(sudoku_cells, 4, 1, 3)
    sudoku_cells[1][4].use(3)
    exclude(sudoku_cells, 3, 1, 4)
    sudoku_cells[1][5].use(1)
    exclude(sudoku_cells, 1, 1, 5)
    sudoku_cells[1][6].use(2)
    exclude(sudoku_cells, 2, 1, 6)
    sudoku_cells[1][7].use(8)
    exclude(sudoku_cells, 8, 1, 7)
    sudoku_cells[1][8].use(6)
    exclude(sudoku_cells, 6, 1, 8)

    dependent_indexes = get_dependent_indexes(sudoku_cells, 6, 1, 8)

    print(dependent_indexes)

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

