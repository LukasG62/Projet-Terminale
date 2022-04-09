## Grando Lukas
##  Module Vehicule

from module_Grille import*
from module_Case import*
from module_exceptions import VehiculeError

class Vehicule:
    
    def __init__(self,nom,couleur, ligne, colonne, sens, longueur) -> None:
        self.__nom=str(nom)
        self.__sens= str(sens)
        
        if self.__sens not in ["H","V"]:
            raise VehiculeError("Vehicule direction must be H or V not " + str(self.__sens))
        
        self.__ligne= int(ligne)
        self.__colonne= int(colonne)
        self.__longueur= int(longueur)
        if self.__longueur <= 1:
            raise VehiculeError("Vehicule size must be at least 2")
        
        self.__couleur = couleur

    def __hash__(self):
        return hash((self.__nom, self.__sens, self.__ligne, self.__colonne))
    
    def __eq__(self, autre):
        return (self.__nom,self.__sens,self.__ligne, self.__colonne, self.__longueur) == (autre.get_nom(),autre.get_sens(), autre.get_ligne(), autre.get_colonne(), autre.get_longueur())
    
    """
    # Méthode de debug
    def __repr__(self):
        return str((self.__nom,self.__sens,self.__ligne, self.__colonne, self.__longueur))
    """
    def get_ligne(self) -> int:
        return self.__ligne
    
    def get_nom(self) -> str:
        return self.__nom
    
    def get_colonne(self) -> int:
        return self.__colonne
    
    def get_longueur(self) -> int:
        return self.__longueur
    
    def get_sens(self):
        return self.__sens
    
    def est_vertical(self) -> bool:
        """
        Description : Prédicat qui retourne vrai si le véhicule est vertical
        """
        return self.__sens=="V"
    
    def est_horizontal(self) -> bool:
        """
        Description : Prédicat qui retourne vrai si le véhicule est horizontal
        """
        return self.__sens=="H"
    
    def change_de_ligne(self,nouvelle_ligne) -> None:
        self.__ligne=int(nouvelle_ligne)

    def change_de_colonne(self,nouvelle_colonne) -> None:
        self.__colonne=int(nouvelle_colonne)
        
    def peut_se_deplacer_vers(self,direction) -> bool:
        """
        Description : Prédicat qui retourne vrai si le déplacement est possible
        Param : Instance de Vehicule, direction (str) la direction dans laquelle le véhicule veut se deplacer
        """
        # Un véhicule vertical ne peut se déplacer que dans les directions Haut et Bas 
        # Un véhicule horizontal ne peut se déplacer que dans les directions Droite et Gauche
        return (
            self.est_vertical() and (direction == "H" or direction == "B") 
            or
            self.est_horizontal() and (direction == "D" or direction == "G")
            )
            
            
    def se_deplacer_vers(self,direction) -> None:
        """
        Description : Méthode qui permet de faire déplacer un véhicule dans la direction passé en paramètre
        Param : direction (str) 
        """
        if direction=="H":
            self.change_de_ligne(self.get_ligne()-1)
            
        if direction=="B":
            self.change_de_ligne(self.get_ligne()+1)
            
        if direction=="G":
            self.change_de_colonne(self.get_colonne()-1)
            
        if direction=="D":
            self.change_de_colonne(self.get_colonne()+1)
            
    def placer_dans_la_grille(self, grille) -> None:
        """
        Description : Méthode qui permet de placer le véhicule dans la grille
        Param : instance de Vehicule, instance de Grille
        S.E : L'instance Grille en paramétre est modifié
        """
        if self.est_vertical():
            for i in range(self.get_longueur()): 
                grille.get_grille()[self.get_ligne()+i][self.get_colonne()].set_content(self.get_nom())
        
        else:
            for i in range(self.get_longueur()):
                grille.get_grille()[self.get_ligne()][self.get_colonne()+i].set_content(self.get_nom())
            
    