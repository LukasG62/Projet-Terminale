from copy import deepcopy
from random import randint

class Pile():
    def __init__(self):
        self.pile = [] # notre pile
        
    def estVide(self):
        return len(self.pile) == 0
    
    def estPresent(self, elt):
        return elt in self.pile
    
    def sommet(self):
        return self.pile[len(self.pile)-1]
    
    def empiler(self, elt):
        self.pile.append(elt)
    
    def depiler(self):
        self.pile.pop()
        
    
laby=[[0,1,0,0,0,0],
      [0,1,1,1,1,0],
      [0,1,0,1,0,0],
      [0,1,0,1,1,0],
      [0,1,1,0,1,0],
      [0,0,0,0,1,0]]

lignes = len(laby) # le nombre de lignes correspondent au nombre de liste dans le tableau
colonnes = len(laby[0]) # le nombre de colonne correspondent à longueur d'une des listes

def voisins(T, v, value = 1):
    """
    fonction qui retourne les coordonnées des voisins proches égaux à 1
    (au dessus et en dessus de lui et sur ses côté s'il existent).
    :param : T un tableau, v des coordonnées dans le tableau T
    :type : list, tuple
    :return: V une liste de coordonnées
    :rtype: list
    """
    V = [] # liste des coordonnée des voisins proches
    i, j = v[0], v[1] # on reporte les coordonnées dans des variables pour alléger l'écriture
    for a in (-1, 1):
        #Pour les lignes
        if 0<=i+1<lignes: # pour éviter les OOR (out of range)    
            if T[i+a][j] == value: # si à la ligne précedente et suivante (signe de a) est 1
                V.append((i+a,j)) # on ajoute dans la liste V ses coordonnées
        #Pour les colonnes
        if 0 <= j+a < colonnes: # pour éviter les OOR (out of range)
            if T[i][j+a] == value: # si à la colonne précedente et suivante (signe de a) est 1
                V.append((i,j+a)) # on ajoute dans la liste V ses coordonnées
    return V

#print(voisins(laby,(0,1)))
"""
En laby[0][1] sur ses côtés il y alaby[0][0] et laby[0][2].
    Les valeurs sont égales à 0 donc la fonction voisins ne les ajoutes pas dans la liste V.
Au dessus de laby, on est hors du tableau donc voisins ne fait rien
En dessous de laby, il y a laby[1][1].
    La valeur est égale à 1 donc voisins l'ajoute dans la liste V
Au final la liste V contient qu'un seul élément les coordonnée de laby[1][1]
"""

def parcours(laby, entree, sortie):
    T = deepcopy(laby) #list
    P = Pile() #object
    v = entree #tuple
    T[v[0]][v[1]] = -1 # quand on visite une case on change sa valeur
    recherche = True
    
    while recherche: 
        vois = voisins(T, v) 
        
        if len(vois) == 0: # Cas ou il n'y pas de voisins proches
            
            if P.estVide(): 
                return False # si vide alors il n'y pas de parcours possible
            
            else:
                P.depiler()
                v = P.sommet()
        else:
            P.empiler(vois[0]) 
            v = P.sommet()
            T[v[0]][v[1]] = -1
            if v == sortie:
                recherche = False 
    return P.pile

print(parcours(laby,(0,1),(5,4)))      
    
def genererLabyrinthe(taille, entree, sortie):
    lignes, colonnes = taille[0], taille[1]
    laby = [[0 for i in range(colonnes)] for i in range(lignes)] 
    v = entree #tuple
    P = Pile() #object
    laby[v[0]][v[1]] = 1
        
            
    