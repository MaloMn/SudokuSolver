import numpy as np
from copy import deepcopy


def format_sudoku(s):
    out = []
    for i in range(0, 81, 9):
        out.append(list(s[i:i+9]))

    out = np.array(out)
    out = out.astype(int)

    return out.tolist()


def line(i, _):
    return [(i, a) for a in range(9)]


def column(_, j):
    return [(a, j) for a in range(9)]


def square(i, j):
    m, n = i//3, j//3
    return [(a, b) for a in range(m*3, m*3+3) for b in range(n*3, n*3+3)]


def gen():
    for i in range(9):
        for j in range(9):
            yield i, j


def check(s):
    """
    Checks whether the sudoku presents mistakes or not.
    It doesn't need to be full to be tested.
    :param s: sudoku to be tested
    :return: True if the sudoku is ok, False if a mistake has been made solving the sudoku
    """
    d = True
    for i, j in gen():
        nb_line = [s[x][y] for x, y in line(i, j) if s[x][y] != 0]
        nb_col = [s[x][y] for x, y in column(i, j) if s[x][y] != 0]
        nb_sq = [s[x][y] for x, y in square(i, j) if s[x][y] != 0]
        for a, b, c in zip(nb_line, nb_col, nb_sq):
            if nb_line.count(a) != 1 or nb_col.count(b) != 1 or nb_sq.count(c) != 1:
                d = False
                print('Problem on cell ({}, {})'.format(i, j))
                break
    return d


def possibilities(s):
    """
    Stores in the poss array the possibles numbers for each empty cell.
    :param s: sudoku
    :return: poss array
    """
    poss = deepcopy(s)

    for i in range(9):
        for j in range(9):
            if s[i][j] == 0:
                a = set()

                for x, y in line(i, j) + square(i, j) + column(i, j):
                    a.add(s[x][y])

                b = {a for a in range(1, 10)}
                poss[i][j] = list(b - a)

    return poss


def P(s):
    """
    Prints the sudoku as a square, so it is easily readable
    :param s: sudoku
    :return: nothing
    """
    p = deepcopy(s)
    p = np.array(p)
    p = p.astype(str)
    p = p.tolist()

    print('\n'.join(['  '.join(a) for a in p]))
    print('\n')


def sole_candidate(s, poss):
    sudoku = deepcopy(s)
    for i in range(9):
        for j in range(9):
            a = poss[i][j]
            if type(a) is list:
                if len(a) == 1:
                    sudoku[i][j] = a[0]

    return sudoku


def make_list_uc(poss, c_list):
    a = [[0, (0, 0)] for i in range(10)]
    for i, j in c_list:
        if type(poss[i][j]) is list:
            for b in poss[i][j]:
                a[b][0] += 1
                a[b][1] = (i, j)
    return a


def unique_candidate(s, poss):
    """
    If there is only one number in one section (line/column/square) in the possibilities, then it chooses that number.
    :param s: sudoku
    :param poss: output of possibilities function
    :return: sudoku
    """
    sudoku = deepcopy(s)
    # For each square
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            occurences = make_list_uc(s, square(i, j))
            for index, a in enumerate(occurences):
                if a[0] == 1:
                    x, y = a[1]
                    sudoku[x][y] = index

    # For each line
    for i in range(9):
        occurences = make_list_uc(s, line(i, 0))
        for index, a in enumerate(occurences):
            if a[0] == 1:
                x, y = a[1]
                sudoku[x][y] = index

    # For each column
    for j in range(9):
        occurences = make_list_uc(s, line(0, j))
        for index, a in enumerate(occurences):
            if a[0] == 1:
                x, y = a[1]
                sudoku[x][y] = index
    return sudoku


def subset(poss, c_list):
    out = []
    # Get the numbers and possibilities for the comprehension list entered
    a = [poss[i][j] for i, j in c_list if type(poss[i][j]) is list]
    for numbers_possible in a:
        if a.count(numbers_possible) == len(numbers_possible) and numbers_possible not in out and len(numbers_possible) > 1:
            out.append(numbers_possible)

    return out


def sub_nb(p, c_list, nb):
    poss = deepcopy(p)

    for x, y in c_list:
        if type(poss[x][y]) is list and poss[x][y] != nb:
            poss[x][y] = list(set(poss[x][y]) - set(nb))

    return poss


def naked_subset(p):
    poss = deepcopy(p)

    # For each square
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # We spot any subset
            nb = subset(poss, square(i, j))
            if len(nb) > 0:
                print(nb, i, j)
            # We remove the numbers in the subset from other positions
            for a in nb:
                poss = sub_nb(poss, square(i, j), a)

    # For each line
    for i in range(9):
        nb = subset(poss, line(i, 0))
        if len(nb) > 0:
            print(nb, i, 0)
        # We remove the numbers in the subset from other positions
        for a in nb:
            poss = sub_nb(poss, line(i, 0), a)

    # For each column
    for j in range(9):
        nb = subset(poss, column(0, j))
        if len(nb) > 0:
            print(nb, 0, j)
        # We remove the numbers in the subset from other positions
        for a in nb:
            poss = sub_nb(poss, column(0, j), a)

    return poss


def won(s):
    w = True
    for l in s:
        if 0 in l:
            w = False
    return w
