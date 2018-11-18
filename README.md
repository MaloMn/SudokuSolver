# SudokuSolver

This is a Sudoku solver. It solves a given Sudoku by trying each possibility until one works.

| | | | | | | | | |
|-|-|-|-|-|-|-|-|-|
|5|3| | |7| | | | |
|6| | |1|9|5| | | |
| |9|8| | | | |6| |
|8| | | |6| | | |3|
|4| | |8| |3| | |1|
|7| | | |2| | | |6|
| |6| | | | |2|8| |
| | | |4|1|9| | |5|
| | | | |8| | |7|9|

## The Rules

*To successfully fill in a Sudoku table, the completed table has to respect the following rules :*
 * *Each and every number, from 1 to 9, must appear once in each line*
 * *Each and every number, from 1 to 9, must appear once in each column*
 * *Each and every number, from 1 to 9, must appear once in each square of 3x3 cells*

## How does it work ?
 * For each empty cell, it creates an array of possible numbers based on the numbers on the corresponding line, column and square.
 * It checks if this action already solved the Sudoku *(easy one)*
 * It then tries to solve it by picking random numbers from each array.

For the moment, __you have to write the tab in the following manner for the program to understand it__:
 * Each empty cell is replaced by a zero,
 * Each line is written next to the previous one on one line.

*Examples*
 * *530070000600195000098000060800060003400803001700020006060000280000419005000080079*
 * *452391876318675294679428315831564729245987163967213548796852431183749652524136987*
 * *608091400009038512213507908004309807001862054302475090820154709945723001137086245*
 * *123456789000000000000000000000000000000000000000000000000000000000000000000000000*
 * *600301059302500000710049800020000467000752000173000020006870014000006903840203005*
 
## What's coming next ?
  * Try to program a more intelligent way of solving it by doing as follow :
    * Each line, column and squared is checked to see if a number of a domain only appears once. If such a number is found, it replaces the previous array.
    * Then, we write in an another array the tree of the possibilties and we test each of them one by one. Before starting, we launch a short test to indicate the user the maximum time it could take to solve the Sudoku (time of checking each possibility)
