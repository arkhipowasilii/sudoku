from sudoku import get_dependent_indexes, main, solve_cell_sudoku


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
    sudoku_cells = main(sudoku)
    return solve_cell_sudoku(sudoku_cells)


if __name__ == '__main__':
    test_get_dependent_indexes()
    test_solve_sudoku()

