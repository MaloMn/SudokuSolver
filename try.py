from functions import *

sudoku = '900700500000910000640000900570040230000103000064080079009000024000098000008001007'

sudoku = format_sudoku(sudoku)
print(check(sudoku))
poss = possibilities(sudoku)
for i in range(100):
    poss = possibilities(sudoku)
    sudoku = sole_candidate(sudoku, poss)

while check(sudoku) and not won(sudoku):
    print('a')
    poss = possibilities(sudoku)
    poss = naked_subset(poss)
    sudoku = sole_candidate(sudoku, poss)

P(sudoku)
