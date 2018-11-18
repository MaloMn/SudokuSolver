# -*- coding: utf-8 -*
import os
import random
from SudokuSolver_Functions import *

while True:
    sudoku = inputSudoku()
    printS(sudoku)
    #if not isCorrect:
        #print("Sorry, this table isn't right")
    ##############################
    ### RESOLUTION PAR DOMAINE ###
    ##############################
    # On calcule les domaines de chacune des cases
    while True:
        sudokuBis = domaine(sudoku)
        if sudokuBis == sudoku:
            # On s'arrête dès que "domaine" ne change rien
            break
        sudoku = sudokuBis.copy()
    printS(sudoku)
    
    if isCorrect(sudoku):
        print("This one was easy, you could have done it!")
    else:
        print("This one is harder than I thought... Would you mind giving me more time ? (YES / NO)")
    
    ############################
    ### RESOLUTION ALEATOIRE ###
    ############################
    os.system('pause')
    
    steps = int(input("Entrez le nombre d'étapes souhaitées : "))
    
    solution = randomSolving(sudoku)
    i = 0
    percent = 0
    while not isCorrect(sudoku) and not isFull(sudoku) and i < steps:
        #print(i)
        solution = randomSolving(sudoku)
        i = i+1
        # On affiche l'avancé de la boucle
        percent = int(100*i/steps)
        if int(100*i/steps) > percent:
            print("{} %".format(percent))
            
    if isCorrect(sudoku) and isFull(sudoku):
        printS(sudoku)
    else:
        print('No solutions')
    ### END OF RESOLUTION ALEATOIRE ###