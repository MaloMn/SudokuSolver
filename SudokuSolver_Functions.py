# -*- coding: utf-8 -*
import random

def inputSudoku():
    """
        Enonce les règles pour entrer la grille de Sudoku
        Demande à l'utilisateur d'entrer la grille
        Vérifie que la grille fait bien 81 nombres
        String to list of arrays
    """
    tab = []
    # We tell the user the rules of the games
    print("How to write your Sudoku Table:")
    print(" - Each empty cell is replaced by a zero")
    print(" - Each line is written next to the previous one")
    print(" - There isn't any spacing whatsoever")
    # We check that there are 81 numbers in "chaine"
    while True:
        try:
            chaine = str(input("Please enter your Sudoku table: "))
        except ValueError:
            print("Sorry I didn't catch that.")
            continue
        if len(chaine) != 81:
            print("There has to be exactly 81 numbers.")
            continue
        if not chaine.isdigit():
            print("Has a Sudoku table ever contained anything else than numbers?")
            continue
        else:
            break
            
    # On met dans tab les nombres inclus dans des listes
    for i in range(len(chaine)):
        tab.append([int(chaine[i])])
    return tab

def eraseIf(liste, element):
    """
        Efface un element d'une liste si la liste le contient
    """
    if element in liste:
        liste.remove(element)
    return liste

def getFirstSquare(A):
    """
        Entrée : coordonnée x ou y d'un point donné
        Donne la coordonné (x ou y en fonction de l'entrée) du point
        haut-gauche du carré dans lequel est le nombre donné
    """
    A = A - A%3
    return A

def domaine(tab):
    """
        Crée les domaines de chaque case de la grille.
        Prends en compte les listes contenant un zéro, et y ajoute les nombres possibles
        possible en prenant en compte les nombres (représenté par des listes de longueur 1)
        sur chaque ligne, colonne et carré.
    """
    tab2 = tab.copy() # On copie le tableau donné pour s'en servir de référence (tab2), !!! tab sera modifié !!!

    for i in range(81):
        smallDomain = []
        # On s'arrête lorsque la case du Sudoku est indiquée vide par un zéro
        if tab[i][0] == 0 or len(tab[i]) > 1:
            smallDomain = [1,2,3,4,5,6,7,8,9] # Au début, chaque nombre est possible
            # On définit la colonne et la ligne de la case i
            C = i % 9
            L = i // 9

            # On test la ligne (RANGE FONCTIONNE)
            # On compare la liste aves les nombres de chaque ligne
            # représentés par des listes de longueur 1 pour que les listes
            # des domaines précédents ([1,2,3]) ne soient pas pris en compte
            for j in range(9*L, 9*L + 9):
                if len(tab2[j]) == 1: # On ne compare que avec les tableaux contenant un unique nombre
                    smallDomain = eraseIf(smallDomain, tab2[j])
                    
            # On test la colonne CONDITION NOT WORKING
            for j in range(C, C + 81, 9):
                if len(tab2[j]) == 1:
                    smallDomain = eraseIf(smallDomain, tab2[j])
            #print('Après colonne : ', smallDomain)
            # On test le carré : on part du coin haut-gauche, et on va ligne par ligne [FONCTIONNE]
            C = getFirstSquare(C)
            L = getFirstSquare(L)

            sum = [0,1,2,9,10,11,18,19,20]
            for j in sum:
                if len(tab2[C + 9*L + j]) == 1:
                    smallDomain = eraseIf(smallDomain, tab2[C + 9*L + j])
            #print('Après carré : ', smallDomain)

        # On ajoute finalement le domaine modifié comme nouveau nombre de la grille
        tab[i] = smallDomain
        if smallDomain == []:
            print("A domain is blank, there's a problem.")
    return tab;

def isCorrect(grille2):
    """
        Regarde si la grille fournie respecte les règles du Sudoku
        Retourne True/False
    """
    res = True
    grille = grille2.copy()
    # On vérifie que la case ne contient qu'un élément
    for i in range(9):
        for j in range(9):
            if not (len(grille[j + i*9]) == 1):
                res = False

    # On enlève les tableaux de la grille
    for i in range(81):
        grille[i] = grille[i][0]

    # On test chaque ligne et chaque colonne ensemble ATTENTION REPETITION, NOT DRY
    for i in range(9):
        dC = [1,2,3,4,5,6,7,8,9]
        dL = [1,2,3,4,5,6,7,8,9]
        for j in range(9):
            # Test de la ligne
            if grille[j + 9*i] not in dL:
                res = False
                break
            else:
                dL.remove(grille[j + 9*i])
            # Test de la colonne
            if grille[i + 9*j] not in dC:
                res = False
                break
            else:
                dC.remove(grille[i + 9*j])
        if res == False:
            break

    # On test le carré
    sum = [0,1,2,9,10,11,18,19,20]
    for L in range(0,9,3):
        for C in range(0,9,3):
            small = [1,2,3,4,5,6,7,8,9]
            for j in sum:
                if grille[C + 9*L + j] not in small:
                    res = False
                    break
                else:
                    small.remove(grille[C + 9*L + j])
            if res == False:
                break
        if res == False:
            break

    return res

def randomSolving(grille):
    """
        Effectue une résolution aléatoire de la grille
    """
    grille2 = grille.copy()
    for i in range(81):
        grille2[i] = random.choice(grille2[i])
    return grille2

def isFull(grille):
    """
        Regarde si la grille comporte 81 nombres, retourne True/False
        ATTENTION : ne vérifie pas qu'elle est correct, utiliser "check"
    """
    b = 0
    for i in range(9):
        for j in range(9):
            if len(grille[i + 9*j]) == 1:
                b += 1
    if b == 81:
        return True
    else:
        return False

def printS(grille):
    """
        Affiche une grille donnée
    """
    b = 0
    c = 0
    a = ""
    for i in range(9):
        a = ""
        if i % 3 == 0:
            print(" ")
        for j in range(9):
            if j % 3 == 0:
                a = a + " "
            a = a + str(grille[j + 9*i])
        print(a)
    print(" ")
