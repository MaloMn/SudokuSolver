from functions import *

sudoku = '002080400000409000093000210940000083000578000700040001026000390000605000010000050'

sudoku = format_sudoku(sudoku)
print(check(sudoku))

while 'before != sudoku':

    before = deepcopy(sudoku)
    poss = possibilities(sudoku)
    poss = naked_subset(poss)
    sudoku = sole_candidate(sudoku, poss)
    sudoku = unique_candidate(sudoku, poss)

    if before == sudoku:
        break

P(sudoku)
