## Grando Lukas
## Module Grille

from module_Case import Case

class Grille:
    
    def __init__(self,largeur = 6, hauteur = 6) -> None:
        self.__largeur = int(abs(largeur))
        self.__hauteur = int(abs(hauteur))
        self.__grille = [ [ Case() for i in range(largeur)] for j in range(hauteur) ]
        self.__exit = None
        
    def get_hauteur(self) -> int:
        return self.__hauteur
    
    def get_largeur(self) -> int:
        return self.__largeur
    
    def set_exit(self, pos_exit):
        self.__exit = pos_exit
    
    def get_grille(self) -> list:
        return self.__grille
    
    def show(self) -> None:
        """
        Description : Méthode qui affiche la grille dans le shell
        Param : Instance de grille
        """
        print("+-"*self.get_largeur()+"+") # bord haut
        for j in range(self.get_hauteur()): # gestion des lignes
            left_side = "|"
            right_side = "|"
            
            for i in range(self.get_largeur()): # gestion des colonnes
                case = self.__grille[j][i]
                
                if (j,i) == self.__exit: # si c'est une sortie
                    right_side = " " # alors sur le bord droit à la position (j,i) est un blanc
                
                print(left_side + case.get_content(),end="") # On affiche le bord gauche et le contenu de la case à la pos (j,i)
                left_side = " " # Pour le reste des case on remplace le bord gauche par un espace
            
            print(right_side) # à la fin de la ligne on affiche le bord droit    
       
        print("+-"*self.get_largeur()+"+") # quand toutes les lignes sont traités on affiche le bords bas
        
    def clear(self) -> None:
        """
        Description : Méthode qui permet de vider chaque case de la grille
        """
        for i in range(self.get_hauteur()):
            for j in range(self.get_largeur()):
                self.__grille[i][j].clear()
        