#
# Ensemble de structure de données crée en autonomie pour faciliter leur utilisation dans l'enseignement "Numérique et sciences informatiques"
# Cependant ce projet n'est pas terminé, il manque certaines méthodes pour les arbres binaires de recherche.
#

class StackError(Exception):
    #Classe representant une erreur de pile héritant de la super classe python "Exception"
    ...

class Pile:
    """
    Description : Classe pour répresenter la struture de donnée des piles
    
    Attribut : 
        hauteur -> int
        sommet -> type du sommet de la pile
        reste -> list 
    Méthodes :
        estVide -> bool
        estPresent -> bool
        sommet -> type du sommet de la pile
        empiler -> None
        depiler -> type du sommet de la pile
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
    
    def get_hauteur(self):
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
    
    def estVide(self) -> bool:
        """
        Description: Prédicat qui renvoie True si la pile est vide
        params : instance de Pile
        """
        return self.__sommet == None
    
    def estPresent(self, elt) -> bool:
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
        while not(self.estVide()):
            self.depiler()

class File:
    """
    Description : Classe pour répresenter la struture de donnée des files
    
    Attribut :
        hauteur -> int
        tete -> type de la tete de la pile
        reste -> list
    
    Méthodes :
        estVide -> bool
        estPresent -> bool
        tete -> type du premier élément de l'attribut file
        queue -> type du dernier élément de l'attribut file
        enfiler -> None
        defiler -> type du dernier élément de l'attribut file
        lireFile -> list
    """
    def __init__(self, liste = None):
        """
        Description: Initialise l'attribut file
        params : liste (list) : paramètre additionnel (par défaut vaut None)
        return : None
        """
        if liste is None or liste == []:
            self.__hauteur = 0
            self.__tete = None
            self.__reste = []
        else:
            self.__hauteur = len(liste)
            self.__tete = liste[0]
            self.__reste = liste[1:]
    
    def get_hauteur(self):
        return self.__hauteur
    
    def get_tete(self):
        return self.__tete
    
    def get_reste(self):
        return self.__reste
    
    def enfiler(self, elt) -> None:
        """
        Description: ajoute un élément dans la file
        params : instance de File, elt
        """
        if self.__hauteur > 0:
            self.__reste.append(elt)
        else:
            self.__tete = elt
        self.__hauteur += 1
    
    def defiler(self):
        """
        Description: supprime un élément dans la file
        params : instance de File
        return : (type du premier élément de la file)
        """
        old_tete = self.__tete #on sauvegarde le sommet pour pouvoir le retourner
        
        #Cas ou la file posséde un reste
        if self.__hauteur > 1:
            self.__tete = self.__reste.pop(0)
            
        #Cas ou la file n'a pas de reste
        elif self.__hauteur == 1:
            self.__tete = None
        
        else:
            #Cas ou file est vide
            raise StackError("Impossible de défiler une file vide !")
        
        self.__hauteur -= 1
        return old_tete
    def estVide(self) -> bool:
        """
        Description: Predicat qui renvoie True si la file est vide
        params : instance de File
        """
        return self.__tete == None
    
    def estPresent(self, elt) -> bool:
        """
        Description: Predicat qui renvoie True si l'élément en paramètre est présent
        params : instance de File, elt (type de l'élément)
        """
        return elt in self.__reste or elt == self.__tete #sans side effect
    
    def clear(self) -> None:
        while not(self.estVide()):
            self.defiler()

class LinkedList:
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        # Comme récupérer la longueur peut être vite complexe autant stocker en mémoire la longueur
        # Ainsi lors de la suppréssion/ajout d'un élément de la liste il suffit de mettre à jour cette valeur
        self.__len = 0
    
    def __len__(self):
        return self.__len
    
    def empty(self):
        """
        Description : Prédicat retournant True si la liste chainée est vide
        """
        return not self.__head
    
    def prepend(self,value):
        """
        Description : Méthode qui ajoute l'élément au début de la liste chainée
        Param : value, l'élément à ajouter
        """
        self.__head = Participant(value, self.__head) # il devient la tête et pointe vers l'ancienne tête
        
        if self.__tail == None: # Si la liste était initialement vide
            self.__tail = self.__head # le Participant devient aussi la queue
        
        else:
            self.__tail.set_target(self.__head) # liste cyclique 
        self.__len +=1 # On incrémente la longueur de la liste
    
    def append(self, value):
        """
        Descritopn : Méthode qui ajoute l'élément à la suite de la liste chainée
        Param : value, l'élément à ajouter
        """
        newNode = Participant(value, self.__head) # Notre liste chainée est cyclique
        
        if self.__head == None: # Si vide alors le noeud est à la fois la tête et la queue
            self.__head = newNode
            self.__tail = newNode
            
        else:
            # Dans le cas contraire la queue initial pointe vers le nouveau Participant et ce dernier devient la queue
            currentTail = self.__tail
            currentTail.set_target(newNode)
            self.__tail = newNode
        
        self.__len +=1 # On incrémente la longueur de la liste
    
    def delete_node(self, node):
        if self.__head != None:
            if self.__head == node:
                if self.__head == self.__tail:
                    self.__head = None
                    self.__tail = None
                
                else:
                    self.__head = self.__head.get_target()
                    self.__tail.set_target(self.__head)
            else:
                previousNode = self.__head
                while previousNode.get_target() != self.__head:
                    if previousNode.get_target() == node:
                        previousNode.set_target(previousNode.get_target().get_target())
                        break
                    else:
                        previousNode = previousNode.get_target()

                if self.__tail == node:
                    self.__tail = previousNode
                    
            self.__len -=1        
    
    def get_tail(self):
        """
        accesseur
        """
        return self.__tail
    
    def get_head(self):
        """
        accesseur
        """
        return self.__head
    

    def __repr__(self):
        affichage = "... -> " + str(self.__head) + " -> "
        if self.__head != None:
            previousNode = self.__head.get_target()
            while previousNode != self.__head and previousNode != None:
                affichage += str(previousNode) + " -> "
                previousNode = previousNode.get_target()
            
            return affichage + "..."
        return "Empty LinkedList"
    
    
    @staticmethod
    def from_list(listToConvert):
        """
        Description : Méthode de classe qui permet de générer une liste chainée à partir d'une liste
        """
        linkedList = LinkedList()
        for elt in listToConvert:
            linkedList.append(elt)
            
        return linkedList
    
    
    def find(self, value):
        if not self.empty():
            if self.__head.get_name() == value:
                return self.__head
            
            currentNode = self.__head.get_target()
            while currentNode != self.__head:
                if currentNode.get_name() == value:
                    return currentNode
                currentNode = currentNode.get_target()
            
        return None
    
    def random_choice(self):
        element = self.__head
        for _ in range(randint(0, len(self))):
            element = element.get_target()
        
        return element
    
class ArbreBinaire:
    
    def __init__(self, value = None, left = None, right = None):
        
        # Si il n'y a qu'un seul argument alors on considère que l'arbre est une feuille
        if left == None and right == None and value != None:
            self.value = value
            self.left = ArbreBinaire()
            self.right = ArbreBinaire()
        else:
            self.value = value 
            self.left = left
            self.right = right
    
    def get_value(self):
        '''accesseur de l'étiquette'''
        return self.value
    
    def get_left(self):
        '''accesseur du sous arbre gauche'''
        return self.left
    
    def get_right(self):
        '''accesseur du sous arbre droit'''
        return self.right
    
    def is_empty(self) -> bool:
        return [self.get_value(),self.get_left(),self.get_right()] == [None, None, None]
    
    def is_leaf(self) -> bool:
        """
        Description : Prédicat qui renvoie True si l'arbre est une feuille
        """
        if self.is_empty():
            return False
        
        else:
            return self.get_left().is_empty() and self.get_right().is_empty()
    
    def has_only_child(self) -> bool:
        """
        Description : Prédicat qui renvoie True si l'arbre n'a qu'un fils
        """
        if self.is_empty():
            return False
        
        return self.get_left().is_empty() ^ self.get_right().is_empty()
    
    def size(self) -> int:
        """
        Description : Méthode qui renvoie le nombre de noeud présent dans l'arbre
        """
        if self.is_empty():
            return 0
        else:
            return 1 + self.get_left().size() + self.get_right().size()
        
    def height(self) -> int:
        """
        Description : Méthode qui renvoie le nombre de niveau présent dans un arbre.
                      On considéreras que la racine a une hauteur de 0
        """
        if self.is_empty():
            return -1
        else:
            return 1 + max(self.get_left().height(), self.get_right().height())
    
    def leaves_count(self) -> int:
        """
        Description : Méthode qui renvoie le nombre de feuilles (noeuds sans fils) présent dans un arbre.
        """
        if self.is_leaf():
            return 1
        else:
            if not(self.is_empty()):
                return 0 + self.get_left().leaves_count() + self.get_right().leaves_count()
            
            return 0
        
    def inode_count(self) -> int:
        """
        Description : Méthode qui renvoie le nombre de noeuds internes présent dans un arbre.
        """
        return self.size() - self.leaves_count()
    
    def invert(self) -> None:
        """
        Description : méthode qui inverse le fils gauche et le fils droit de l'arbre binaire
        SIDE-EFFECT : L'objet arbre est modifié
        """
        if not self.is_empty():
            self.left, self.right = self.right, self.left
            self.right.invert()
            self.left.invert()
            
    def breadth_first_search(self) -> list: #Parcours en largeur
        to_process = File()
        to_process.enfiler(self)
        route = []
        while not to_process.estVide():
            curr_node = to_process.defiler()
            
            if not(curr_node.get_left().is_empty()):
                to_process.enfiler(curr_node.get_left())
            
            if not(curr_node.get_right().is_empty()):
                to_process.enfiler(curr_node.get_right())
            
            route.append(curr_node.get_value())
        return route
    
    def inorder(self) -> list:
        if self.is_empty():
            return []
        else:
            return self.get_left().inorder() + [self.get_value()] + self.get_right().inorder()
    
    def postorder(self) -> list:
        if self.is_empty():
            return []
        else:
            return self.get_left().postorder() + self.get_right().postorder() + [self.get_value()]
    
    def preorder(self) -> list:
        if self.is_empty():
            return []
        else:
            return [self.get_value()] + self.get_left().preorder() + self.get_right().preorder()

    def is_bst(self) -> list:
        return self.inorder() == sorted(self.inorder())



class BinarySearchTree(ArbreBinaire):
    def __init__(self, value = None, left = None, right = None):
        if left == None and right == None and value != None:
            self.value = value
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        else:
            self.value = value 
            self.left = left
            self.right = right
        
        if not self.is_bst():
            raise Exception("Not a bst")
        
        
        
    def search_value(self,cleRecherchee):
        if self.is_empty():
            return False
        
        else:
            if cleRecherchee == self.get_value():
                return True
            else:
                if cleRecherchee < self.get_value():
                    return self.get_left().search_value(cleRecherchee)
                else:
                    return self.get_right().search_value(cleRecherchee)
    
    def insert(self,valeur):
        if self.is_empty():
            self.__init__(valeur)
        else:
            if valeur < self.get_value():
                self.get_left().insert(valeur)
            elif valeur > self.get_value():
                self.get_right().insert(valeur)
            else:
                raise Exception("Node value already in BST")
    
    def insert_list(self,liste):
        for elt in liste:
            self.insert(elt)
    
    def delete(self,noeud):
        pass # TODO
    
    def way_to(self,cle):
        pass # TODO
        
    def min_value(self):
        if self.is_leaf():
            return self.get_value()
        else:
            return self.get_left().min_value()
        
    def max_value(self):
        if self.is_leaf():
            return self.get_value()
        else:
            return self.get_right().max_value()
    
    

if __name__ == '__main__':
    pommier = ArbreBinaire(4,ArbreBinaire(7),ArbreBinaire(9,ArbreBinaire(2),ArbreBinaire(3)))
    print("Taille - ", pommier.size())
    print("Hauteur - ", pommier.height())
    print("Nombre de feuilles - ", pommier.leaves_count())
    print("Nombre de noeuds internes - ", pommier.inode_count())
    print("Parcours en largeur :")
    print("\t " + str(pommier.breadth_first_search()))
    print("Parcours en profondeur : ")
    print("\t infixe : ")
    print("\t\t " + str(pommier.inorder()))
    print("\t postfixe : ")
    print("\t\t " + str(pommier.postorder()))
    print("\t prefixe : ")
    print("\t\t " + str(pommier.preorder()))
    
    print("ABR")
    peuplier = BinarySearchTree(9, BinarySearchTree(8, BinarySearchTree(3),BinarySearchTree()), BinarySearchTree(12,BinarySearchTree(), BinarySearchTree(15)))
    
    
