from functions import *

sudoku = '002840005500001004004005006030000010000504000090000080700200900200900008900086300'

sudoku = format_sudoku(sudoku)
print(check(sudoku))
poss = possibilities(sudoku)
for i in range(100):
    poss = possibilities(sudoku)
    sudoku = sole_candidate(sudoku, poss)

for i in range(20):
    print('a')
    poss = possibilities(sudoku)
    poss = naked_subset(poss)
    sudoku = sole_candidate(sudoku, poss)

P(sudoku)
