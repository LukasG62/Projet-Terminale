## Grando Lukas
## Module Jeu

from copy import deepcopy
from time import time, sleep

from module_Flotte import Flotte
from module_Grille import Grille
from module_Vehicule import Vehicule
from module_exceptions import BadLevelFileError

from os import listdir # Pour pouvoir récupérer une liste avec les noms des fichiers dans un répertoire

class Jeu:
    DESC = "Le but du jeu et de déplacer la voiture A vers le bord droit du plateau où se trouve la sortie pour la libérer des bouchons en un minimum de coup qui correspondra à votre score.\n La commande pour déplacer un véhicule est composé de 2 lettres :\n - la 1er correspond à la lettre du véhicule\n - la 2eme correspond à la lettre de la direction (H)aut, (B)as, (G)auche, (D)roite"
    
    def __init__(self) -> None:
        self.__fleet = Flotte() # dico
        self.__grille = Grille() # Grille
        self.__exit = None
        self.__deplacement = 0 # int
        self.__levels = [level for level in listdir("niveau") if level[-4:] == ".lvl"] # On ajoute que les noms de fichier ayant l'extension .lvl
        
        if len(self.__levels) == 0: # Si il n'y a aucun niveau dans le fichier
            raise LevelsDirectoryError("Need at least 1 level in directory")
        
        self.__current_level = 0
        
    def play(self) -> None:
        """
        Description : Méthode qui permet de jouer au Rush Hour
        """
        print(Jeu.DESC)
        veut_jouer = True
        while veut_jouer:
            self.__grille.clear() # vidage de la grille
            self.__fleet = Flotte() # vidage de la flotte
            print("Chargement du niveau " + str(self.__current_level))
            self.load_level("niveau/" + self.__levels[self.__current_level])
            self.__grille.show()
            self.__deplacement = 0
            
            while not self.is_finish():
                user_input = "404"
                
                while not(self.can_move(user_input)) and user_input != "SOLVE":
                    user_input = input("Saisir la commande de déplacement : ").upper()
                
                # Intégration de la méthode pour résoudre le puzzle pour pouvoir tester en jeu (à voir si définitif)
                if user_input == "SOLVE":
                    self.afficher_solution(self.solve())
                
                else:
                    self.__fleet.get_vehicule(user_input[0]).se_deplacer_vers(user_input[1])
                    self.__grille.clear()
                    self.__fleet.place_fleet(self.__grille)
                    self.incrementer_le_nb_de_deplacements()
                self.__grille.show()
            
            print("Bravo vous êtes sorti(e) des bouchons en " + str(self.__deplacement) + " déplacement(s) félicitation")
            user_input = input("Voulez vous passez au niveau suivant ? Y/N ").upper()
            
            if user_input == "Y":
                self.next_level()
                
                if self.__current_level == len(self.__levels):
                    print("Vous avez fini tous les niveaux ! Fermeture du jeu")
                    self.__current_level = 0
                    veut_jouer = False
            
            else:
                veut_jouer = False
                print("bye bye")
    
    def define_exit(self) -> None:
        """
        Description : Méthode pour définir la sortie en fonction de l'emplacement du véhicule A
        """
        self.__exit = (self.__fleet.get_vehicule("A").get_ligne(),self.__grille.get_largeur()-self.__fleet.get_vehicule("A").get_longueur())
        self.__grille.set_exit(self.__exit)
    
    def load_level(self, directory = "niveau/niveau0.lvl") -> None:
        """
        Description : Méthode qui permet de charger un niveau selon le contenu d'un fichier
        Param : Instance de Jeu, directory (str) le chemin du fichier niveau
        """
        file = open(directory, "r") # ouverture en mode lecture
        file_content = file.read().split("\n") # ajout de chaque ligne dans une liste
        file.close()
        
        if file_content[len(file_content)-1][0] != "#" and file_content[0][0] != "#":
            raise BadLevelFileError("Levels must be mark out by \"#\"")
        
        del file_content[len(file_content)-1]; del file_content[0] # on supprime les lignes inutiles
        
        for elt in file_content: # pour chaque ligne du fichier
            temp = elt.split(",") # séparation des paramètre du véhicule
            if len(temp) != 6:
                raise BadLevelFileError("Information missing : " + str(len(temp)) + "instead of 6") # on lève une erreur
            
            self.__fleet.add_vehicule(Vehicule(temp[0], temp[1], temp[2], temp[3],temp[4], temp[5])) # creation du véhicule dans la flotte
            
        if "A" not in self.__fleet: # si il nous manque le véhicule à faire sortir
            raise BadLevelFileError("Level needed a car labeled \"A\"")
        
        self.define_exit()
        self.__fleet.place_fleet(self.__grille) # on place tous les véhicules dans la grille
    
    def next_level(self) -> None:
        self.__current_level += 1
        
    
    def can_move(self, user_input) -> bool:
        """
        Description : Prédicat qui retourne vrai si le véhicule peut bouger dans la direction passé en paramètre
        Param : Instance de Jeu, user_input (str) une direction
        """
        if len(user_input) == 2:
            car_name, direction = user_input[0], user_input[1] # On sépare la commande
        
            if car_name in self.__fleet: # on vérifie que l'utilisateur veut déplacer un véhicule éxistant
                if self.__fleet.get_vehicule(car_name).peut_se_deplacer_vers(direction): # on vérifie si ce véhicule peut bien de déplacer selon son orientation
                    car = self.__fleet.get_vehicule(car_name)
                    
                    if car.est_vertical():
                        if direction == "H" and car.get_ligne() != 0: # si le véhicule n'est pas sur le bord haut de la grille
                            return self.__grille.get_grille()[car.get_ligne()-1][car.get_colonne()].is_blank() # et qu'il n'a pas de véhicule au dessus de lui alors il peut se déplacer
                        
                        elif direction == "B" and car.get_ligne()+car.get_longueur() != self.__grille.get_largeur(): # si le véhicule ne touche pas le bord bas de la grille
                            return self.__grille.get_grille()[car.get_ligne()+car.get_longueur()][car.get_colonne()].is_blank() # et qu'il n'y a pas de véhicule en dessous de lui alors il peut se déplacer
                        
                        return False 
                    
                    # même raisonnement pour un véhicule horizontal 
                    elif self.__fleet.get_vehicule(car_name).est_horizontal():
                        if direction == "G" and car.get_colonne() != 0:
                            return self.__grille.get_grille()[car.get_ligne()][car.get_colonne()-1].is_blank()
                        
                        elif direction == "D" and car.get_colonne()+car.get_longueur() != self.__grille.get_hauteur():
                            return self.__grille.get_grille()[car.get_ligne()][car.get_colonne()+car.get_longueur()].is_blank()
                            
                        return False
                
                return False
            
            return False
        
        return False
    
    def incrementer_le_nb_de_deplacements(self) -> None:
        self.__deplacement += 1
    
    
    def is_finish(self) -> bool:
        """
        Description : Prédicat qui retourne vrai si le véhicule A est sur la case de sortie 
        """
        return self.__fleet.get_vehicule("A").get_colonne() == self.__exit[1]
    
    def neighbour_list(self) -> list:
        """
        Description : Méthode qui permet de générer la liste de toutes les situation voisine à la situation initial préalablement chargé
        """
        neighbour = []
        
        for car in self.__fleet.get_fleet().values(): # on récupére tous les véhicules
            for direction in ["H","B","G","D"]:
                if self.can_move(car.get_nom() + direction): # Si on peut le déplacer dans une direction
                    new_config = deepcopy(self.__fleet) # copie de notre flotte ainsi que les objets (on utilise ici deepcopy pour éviter de copier la référence des véhicules)
                    #print("nouvelle configuration")
                    new_config.get_vehicule(car.get_nom()).se_deplacer_vers(direction) # on deplace le véhicule dans la direction possible
                    neighbour.append(new_config) # ce qui nous donne une nouvelle situation qu'on ajoute dans notre liste
                        
        return neighbour
    
    def show(self) -> None:
        """
        Description : Méthode qui permet d'afficher la grille
        """
        return self.__grille.show()
    
    def solve(self) -> list:
        """
        Description : Méthode qui permet de résoudre un niveau préalablement chargé et qui retourne la liste des commandes à effectuer pour gagner la partie
        """
        init_fleet = deepcopy(self.__fleet) # sauvegarde de la flotte initial pour éviter les effets de bord
        candidates = [self.__fleet] # situation à traiter
        seen = {self.__fleet:None}
        found = False
        debut = time() # On lance notre chrono
        while candidates != [] and found != True: # Tant que toutes les situations ne sont pas traité ou qu'on a pas trouvé la sortie
            current = candidates.pop(self.best_situation_index(candidates)) # on sort la situation la plus favorable (càd une situation ou le véhicule A est le plus proche de la sortie)
            
            if self.is_finish():
                found = True
            
            else:
                self.__grille.clear() # On efface la grille
                self.__fleet = current # On remplace notre flotte
                self.__fleet.place_fleet(self.__grille)
                #self.__grille.show()
                for neighbour in self.neighbour_list(): # pour toutes les situations voisines
                
                    if neighbour not in seen: # si c'est une nouvelle situation
                        seen[neighbour] = current # On l'enregistre en précisant son parent (càd la situation que l'on traite) 
                        candidates.append(neighbour) # on l'ajoute dans les situations à traiter
            
        if found:
            fin = time() # on arrete le chrono
            print("Solution trouvé")
            print(str(len(seen)) + " situations testées " + " en " + str(round(fin-debut,3)) + "s") # On affiche le nombre de situation traité ainsi que le temps
            # Retour à l'état initial
            self.__fleet = init_fleet
            self.__grille.clear()
            self.__fleet.place_fleet(self.__grille)
            print("Affichage de la solution ...")
            return self.build_solution(current, seen) # On remonte notre dict
        
        else:
            raise Exception("RushHour impossible ?")
    
    def build_solution(self, current, seen) -> list:
        """
        Descriptions : Méthode qui permet de reconstruire la liste des situation qui améne à une victoire
        Param : Instance de Jeu, current (dict) une flotte de véhicule, seen (dict)
        """
        path = [] # chemin des situations 
        fleet = current
        while fleet != None: # tant que la flotte n'est pas celle de la situation initial
            fleet = seen[fleet] # on récupère son parent
            path.append(fleet) # on l'ajoute à notre chemin
        
        path = list(reversed(path[:-1])) # on inverse le chemin et on enlève le parent vide
        return self.generate_list_command(path)
    
    def get_command_from(self, vehicule_s1, vehicule_s2) -> str:
        """
        Description : Méthode qui permet de récupérer la commande de déplacement d'un véhicule
        Param : vehicule_s1 (Vehicule), vehicule_s2 (Vehicule)
        """
        if vehicule_s1.est_vertical(): # Cas d'un véhicule vertical
            
            if vehicule_s2.get_ligne() > vehicule_s1.get_ligne(): # Si la ligne du véhicule de la situation suivante est plus grande
                return vehicule_s1.get_nom()+"B" # Alors il s'est déplacé vers le bas
            
            else: # Sinon c'est forcement un déplacement vers le haut
                return vehicule_s1.get_nom()+"H"
        else:
            # Cas d'un véhicule horizontal
            if vehicule_s2.get_colonne() > vehicule_s1.get_colonne(): # Si la colonne du véhicule de la situation suivante est plus grande
                return vehicule_s1.get_nom()+"D" # Alors il s'est déplacé vers la droite
            
            else: # Sinon c'est forcement un déplacement vers la gauche
                return vehicule_s1.get_nom()+"G"
    
    def generate_list_command(self, liste_situations) -> list:
        """
        Description : Méthode qui permet de générer la liste des commandes pour passer d'une situation à une autre
                      dans une liste de situation
        Param : Instance de Jeu, liste_situation (str) contenant des flottes (dict)
        """
        liste_commande = []
        
        for i in range(len(liste_situations)-1): # Parcours des situations sauf le dernier
            prev_fleet = liste_situations[i] # la flotte de la situation précédente
            next_fleet = liste_situations[i+1] # la flotte de la situation suivante
            
            for vehicule_name in prev_fleet: # Parcours des clés de la flotte
                
                if prev_fleet.get_vehicule(vehicule_name) != next_fleet.get_vehicule(vehicule_name): # Si les véhicules sont différent
                    #print(prev_fleet[vehicule_name],next_fleet[vehicule_name])
                    liste_commande.append(self.get_command_from(prev_fleet.get_vehicule(vehicule_name),next_fleet.get_vehicule(vehicule_name))) # on utilise notre méthode
                    break # C'est le seul véhicule qui s'est déplacé car situation = 1 déplacement 
        print("Nombre de coup : " + str(len(liste_commande)))
        
        return liste_commande

    def best_situation_index(self, liste_situation):
        """
        Description : Méthode qui retourne l'index de la meilleur situation parmis une liste de situation.
                      La meilleur situation est la situation dans laquelle le véhicule A est le plus proche de la sortie
        Param : Instance de Jeu, liste_situation (list) contenant des flottes (dict)
        """
        if liste_situation != []: # Pour une liste non vide
            best_index = 0 # On postule que l'indice de la meilleur situation est 0
            
            for i in range(1,len(liste_situation)): # Pour chaque situation sauf le 1er étant pour l'instant le meilieur
                
                if liste_situation[i].get_vehicule("A").get_colonne() > liste_situation[best_index].get_vehicule("A").get_colonne(): # si la situation à l'indice i et la meilieur
                    best_index = i # son indice devient le meilieur
        
            return best_index
        raise Exception("Empty list have no index")
    
    def afficher_solution(self,liste_commande):
        for elt in liste_commande:
            self.__fleet.get_vehicule(elt[0]).se_deplacer_vers(elt[1])
            self.__grille.clear()
            self.__fleet.place_fleet(self.__grille)
            self.incrementer_le_nb_de_deplacements()
            for _ in range(50):
                print()
            self.__grille.show()
            sleep(0.5)
if __name__ == "__main__":
    J = Jeu()
    #J.load_level("niveau/niveau3.lvl")

    