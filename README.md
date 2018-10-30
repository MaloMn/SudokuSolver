# SudokuSolver

This is a sudoku solver. It solves a given sudoku by trying each possibility until one works.

[5][3][ ] [ ][7][ ] [ ][ ][ ]
[6][ ][ ] [1][9][5] [ ][ ][ ]
[ ][9][8] [ ][ ][ ] [ ][6][ ]

[8][ ][ ] [ ][6][ ] [ ][ ][3]
[4][ ][ ] [8][ ][3] [ ][ ][1]
[7][ ][ ] [ ][2][ ] [ ][ ][6]

[ ][6][ ] [ ][ ][ ] [2][8][ ]
[ ][ ][ ] [4][1][9] [ ][ ][5]
[ ][ ][ ] [ ][8][ ] [ ][7][9]

Règles :
 - Tous les nombre de 1 à 9 sur chaque ligne, chaque colonne, et dans chaque carré.
 - Chaque nombre ne peut donc apparaître qu'une seule fois sur ces mêmes ensembles.

MODELE DE GRILLE A FOURNIR AU PROGRAMME : 530070000600195000098000060800060003400803001700020006060000280000419005000080079

FONCTIONNEMENT DU PROGRAMME :
  - On recherche le domaine de chaque case
  - On tente une approche hasardeuse pour trouver la solution