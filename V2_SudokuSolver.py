from functions import *

sudoku = '900700500000910000640000900570040230000103000064080079009000024000098000008001007'

sudoku = format_sudoku(sudoku)
print('original')
P(sudoku)



print('sole_candidate')
for i in range(100):
    poss = possibilities(sudoku)
    sudoku = sole_candidate(sudoku, poss)
P(sudoku)

for i in poss:
    print(i)

for i in range(100):
    poss = possibilities(sudoku)
    sudoku = unique_candidate(sudoku, poss)
print('unique_candidate')

poss = naked_subset(poss)

for i in poss:
    print(i)