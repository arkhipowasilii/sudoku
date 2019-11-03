from sudoku import get_dependent_indexes, main, get_next_indexes, get_prev_indexes


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


if __name__ == '__main__':
    test_get_dependent_indexes()

