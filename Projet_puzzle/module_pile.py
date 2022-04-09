## Grando Lukas
## Pile POO d'après le modéle de Mr.Coste (càd 3 attributs : hauteur, sommet, reste)

class StackError(Exception):
    #Classe representant une erreur de pile héritant de la super classe python "Exception"
    ...

class Pile:
    """
    Description : Classe pour répresenter la struture de donnée des piles
    
    Attributs privé :
        hauteur -> int : Le nombre d'élément dans la pile
        sommet -> any : Le dernier élément de la pile
        reste -> list : Tous les élément de la pile sauf le dernier
        
        
    Méthodes :
        est_vide -> bool
        est_present -> bool
        get_sommet -> any
        get_hauteur -> int
        empiler -> None
        depiler -> any
    """
    def __init__(self, liste = None) -> None:
        """
        Description: Initialise l'attribut pile
        params : liste (list) : paramètre additionnel (par défaut vaut None)
        return : None
        """
        if liste is None or liste == []:
            self.__hauteur = 0
            self.__sommet = None
            self.__reste = []
        else:
            self.__hauteur = len(liste)
            self.__sommet = liste[-1]
            self.__reste = liste[:-1]
    
    def get_hauteur(self) -> int:
        return self.__hauteur
    
    def get_sommet(self):
        return self.__sommet
    
    def __repr__(self) -> str:
        if self.__sommet == None:
            return "Pile Vide"
        
        repr_pile = "-> " + str(self.__sommet) + "\n" # On indique le sommet avec une fléche
        for elt in reversed(self.__reste): # on parcours dans le sens inverse le reste (LIFO)
            repr_pile += "   " + str(elt) + "\n" # On concatène l'élément du reste 
        
        return repr_pile
        
    def est_vide(self) -> bool:
        """
        Description: Prédicat qui renvoie True si la pile est vide
        params : instance de Pile
        """
        return self.__sommet == None
    
    def est_present(self, elt) -> bool:
        """
        Description: Prédicat qui renvoie True si elt est dans la pile
        params : instance de Pile, elt
        """
        return elt in self.__reste or self.__sommet == elt #pour éviter un side effect
    
    
    def empiler(self, valeur) -> None:
        """
        Description: ajoute un élément dans la pile
        params : instance de Pile, elt
        """
        if self.__hauteur > 0:
            # Le sommet de la pile passe dans le reste
            self.__reste.append(self.__sommet)
        # le nouveau sommet est la valeur qu'on empile
        self.__sommet = valeur
        # La hauteur de la pile augmente de 1
        self.__hauteur += 1
    
    def depiler(self):
        """
        Description: supprime le sommet de la pile
        params : instance de Pile
        return : (type du dernier élément de la pile)
        """
        old_sommet = self.__sommet #on sauvegarde le sommet pour pouvoir le retourner
        
        #Cas ou la pile posséde un reste
        if self.__hauteur > 1:
            self.__sommet = self.__reste.pop()
            
        #Cas ou la pile n'a pas de reste
        elif self.__hauteur == 1:
            self.__sommet = None
        
        else:
            #Cas ou pile est vide
            raise StackError("Impossible de dépiler une pile vide !")
        
        #Dans tous les cas (hors exception) on décrémente la hauteur et on retourne l'ancien sommet
        self.__hauteur -= 1
        return old_sommet
    
    def clear(self) -> None:
        while not(self.est_vide()):
            self.depiler()
