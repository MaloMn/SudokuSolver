import random

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
        Donne la coordonné (x ou y en fonction de l'entrée) du point haut-gauche du carré dans lequel est le nombre donné
    """
    A = A - A%3
    return A

def domaine(tab):
    """
        Crée les domaines de chaque case de la grille
    """
    tab2 = tab.copy() # On copie le tableau donné pour s'en servir de référence (tab2), tab sera modifié
    
    for i in range(len(tab2)):
        smallDomain = []
        # On s'arrête lorsque la case du Sudoku est indiquée vide par un zéro
        if tab[i] == 0:
            smallDomain = [1,2,3,4,5,6,7,8,9] # Au début, chaque nombre est possible. On va enlever progressivement les nombres qui sont déjà compris
            C = i % 9
            L = i // 9
            
            # On test la ligne (RANGE FONCTIONNE)
            for j in range(9*L, 9*L + 9):
                smallDomain = eraseIf(smallDomain, tab2[j])
                #print('j = ', j, 'case = ',tab2[j])
                
            #print('Après ligne : ', smallDomain)
            # On test la colonne (RANGE FONCTIONNE)
            for j in range(C, C + 81, 9):
                smallDomain = eraseIf(smallDomain, tab2[j])
            #print('Après colonne : ', smallDomain)
            # On test le carré : on part du coin haut-gauche, et on va ligne par ligne [FONCTIONNE]
            C = getFirstSquare(C)
            L = getFirstSquare(L)

            sum = [0,1,2,9,10,11,18,19,20]
            for j in sum:
                smallDomain = eraseIf(smallDomain, tab2[C + 9*L + j])
            #print('Après carré : ', smallDomain)
        else:
            # Si la grille contient déjà un nombre, on le converti en liste d'un élément.
            smallDomain.append(tab2[i])
            
        # On ajoute finalement le domaine modifié comme nouveau nombre de la grille
        tab[i] = smallDomain
        #print(smallDomain)
    return tab;
    
def isCorrect(grille2):
    """
        Regarde si la grille fournie respecte les règles du Sudoku
        Retourne True/False
    """
    grille = grille2.copy()
    # On vérifie que la case ne contient qu'un élément
    for i in range(9):
        for j in range(9):
            if len(grille[j + i*9]) == 1:
                res = True
            else:
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
    a = ""
    for i in range(9):
        a = ""
        for j in range(9):
            a = a + str(grille[j + 9*i])
        print(a)