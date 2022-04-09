class Flotte:
    def __init__(self, dict_vehicule = None):
        if dict_vehicule == None:
            self.__fleet = {}
        
        else:
            self.__fleet = dict_vehicule
        
    def get_fleet(self):
        return self.__fleet
    
    def add_vehicule(self, vehicule):
        self.__fleet[vehicule.get_nom()] = vehicule
        
    def get_vehicule(self, nom_vehicule):
        return self.__fleet[nom_vehicule]
    
    def est_vide(self):
        return self.__fleet == {}
    
    def place_fleet(self,grille) -> None:
        """
        Description : Méthode qui permet de placer un véhicule dans la grille
        """
        for vehicule in self.__fleet.values():
            vehicule.placer_dans_la_grille(grille)
    
    def __eq__(self, autre_flotte):
        if isinstance(autre_flotte, Flotte):
            return self.__fleet == autre_flotte.get_fleet()
        
        return False
    
    def __hash__(self):
        return hash(tuple(sorted(self.__fleet.items())))
    
    def __iter__(self):
        return self.__fleet.__iter__()
            
    
        
    
    
        
    
    
        
    
    