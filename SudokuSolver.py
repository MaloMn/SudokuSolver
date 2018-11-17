# -*- coding: utf-8 -*
import os
import random
from SudokuSolver_Functions import *

while True:
    sudoku = inputSudoku()
    printS(sudoku)
    
    ##############################
    ### RESOLUTION PAR DOMAINE ###
    ##############################
    # On calcule les domaines de chacune des cases
    while True:
        sudokuBis = domaine(sudoku)
        printS(sudokuBis)
        if sudokuBis == sudoku:
            # On s'arrête dès que "domain" ne change rien
            break
        sudoku = sudokuBis.copy()
    
    ############################
    ### RESOLUTION ALEATOIRE ###
    ############################
    os.system('pause')
    
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