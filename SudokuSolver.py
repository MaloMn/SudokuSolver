import os
import random
from SudokuSolver_Functions import *
    
chaineSudoku = ''
sudoku = []
smallDomain = []

# Demande à l'utilisateur de la chaîne de caractère représentant la grille de sudoku
chaineSudoku = str(input('Entrez la grille de sudoku à résoudre (écrivez les chiffres de la grille ligne par ligne, sans espace, en mettant un zéro si la cas est vide) : '));
while len(chaineSudoku) != 81:
    chaineSudoku = str(input('Vous avez commis une erreur. Merci de réessayer (écrivez les chiffres de la grille ligne par ligne, sans espace, en mettant un zéro si la cas est vide) : '));
    
steps = int(input("Entrez le nombre d'étapes souhaitées : "))

# Transformation de la chaîne de caractère en tableau
# Sudoku contient maintenant un tableau

for i in range(len(chaineSudoku)):
    sudoku.append(int(chaineSudoku[i])) # On transforme les caractères en nombres

# On calcule les domaines de chacune des cases
sudoku = domaine(sudoku)
print(sudoku)
# RESOLUTION ALEATOIRE
solution = randomSolving(sudoku)
test = check(solution)
i = 0
while not test and i < steps:
    #print(i)
    solution = randomSolving(sudoku)
    test = check(solution)
    i = i+1
    
if test:
    print("Hurray!") ### AFFICHER CONVENABLEMENT LA grille
else:
    print('No solutions')

os.system("pause")