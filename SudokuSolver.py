# -*- coding: utf-8 -*

import random
from SudokuSolver_Functions import *

while 1 == 1:
    chaineSudoku = ''
    sudoku = []
    smallDomain = []
    res = True

    # Demande à l'utilisateur de la chaîne de caractère représentant
    # la grille de sudoku
    chaineSudoku = inputSudoku()
    
    ##############################
    ### RESOLUTION PAR DOMAINE ###
    ##############################
    # On calcule les domaines de chacune des cases
    sudoku = domaine(sudoku)
    
    ############################
    ### RESOLUTION ALEATOIRE ###
    ############################
    steps = int(input("Entrez le nombre d'étapes souhaitées : "))
    
    solution = randomSolving(sudoku)
    i = 0

    while not isCorrect(sudoku) and not isFull(sudoku) and i < steps:
        #print(i)
        solution = randomSolving(sudoku)
        i = i+1

    if isCorrect(sudoku) and isFull(sudoku):
        printS(sudoku)
    else:
        print('No solutions')
    ### END OF RESOLUTION ALEATOIRE ###