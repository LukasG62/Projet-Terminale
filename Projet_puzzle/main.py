## Grando Lukas
## Projet puzzle POO

from math import sqrt
from random import choice, shuffle
from time import time

from module_pile import Pile
from module_tuile import Tile
from module_exception import *  

class Puzzle:
    def __init__(self, tiles) -> None:
        
        if sqrt(len(tiles)) != float(int(sqrt(len(tiles)))): # on vérifie qu'on a bien un carré oarfait
            raise DimensionError("Puzzle must be a square")
        
        self.__height = int(sqrt(len(tiles)))
        self.__width = int(sqrt(len(tiles)))
        self.__tiles = tiles
        self.__movement = Pile()
    
    
    def __hash__(self):
        return hash(tuple(self.__tiles))
    
    def __eq__(self, autre):
        if isinstance(autre, Puzzle):
            return self.__tiles == autre.get_tiles()
        
        return False
    
    def display(self) -> None:
        """
        Description : Affiche le puzzle
        """
        sep_line = "+----"*self.__width + "+"
        
        for y in range(self.__height):
            print(sep_line)
            line = ""
            for x in range(self.__width):
                value = self.__tiles[x+y*self.__width].get_value()
                if value != " " and int(value) >= 10:
                    line += "| " + self.__tiles[x+y*self.__width].get_value() + " "
                else:
                    line += "|  " + self.__tiles[x+y*self.__width].get_value() + " "
            
            print(line + "|")
            
        print(sep_line)
            
    def get_height(self) -> int:
        return self.__height
    
    def get_width(self) -> int:
        return self.__width
    
    def get_tiles(self) -> list:
        return self.__tiles
    
    def get_blank(self) -> bool:
        """
        Descripiton : méthode retournant la position du trou dans le puzzle
        params : Instance de Puzzle
        """
        for i in range(len(self.get_tiles())):
            if self.get_tiles()[i].is_blank():
                return i
        
        raise Exception("No blank ?")
    
    def set_tiles(self, new_tiles) -> None:
        """
        Description : mutateur de self.__tiles
        Param : new_tiles (list), une liste de tuile
        """
        self.__tiles = new_tiles
        
    def tiles_well_placed(self) -> int:
        """
        Description : Methode qui retourne le nombre de tuile bien placé dans le puzzle
        """
        res = 0
        tiles = self.get_tiles()
        for i in range(len(tiles)-1):
            if tiles[i].get_value() == str(i+1):
                res += 1
        if tiles[len(tiles)-1].get_value() == " ":
            res += 1
        
        return res
    
    def is_finish(self) -> bool:
        """
        Description : Prédicat retournant vrai si le puzzle est résolu
        """
        return self.tiles_well_placed() == len(self.get_tiles())
    
    
    def enum_direction(self) -> list:
        """
        Description : Méthode qui retourne toutes les directions possibles pour le trou
        """
        
        #conversion de la position dans la liste de tuile en coordonnées
        trou_index = self.get_blank()
        x, y = trou_index % self.__width, trou_index // self.__width
        
        direction = []
        
        if y != 0:
            direction.append("H")
        
        if x != 0:
            direction.append("G")
            
        if x != self.__width-1:
            direction.append("D")
        
        if y != self.__height-1:
            direction.append("B")
        
        return direction



    def move_blank_to(self, direction) -> None:
        """
        Description : Méthode qui déplace le trou vers la direction passé en paramètre
        Param : direction (str) une des directions possible
        """
        tiles = self.__tiles
        possible_directions = self.enum_direction()
        
        blank_index = self.get_blank()
        x, y = blank_index % self.__width, blank_index // self.__width
        
        if direction not in possible_directions: # si la direction n'est pas possible
            raise MovementError("Can't move to " + direction) # on lève une erreur
        
        else:
            if direction == "H": # Si on déplace le trou vers le haut
                # on permute la position du trou avec la tuile au desssus
                tiles[blank_index], tiles[x+(y-1)*self.__width] = tiles[x+(y-1)*self.__width], tiles[blank_index]
        
            elif direction == "B":
                # on permute la position du trou avec la tuile au desssous
                tiles[blank_index], tiles[x+(y+1)*self.__width] = tiles[x+(y+1)*self.__width], tiles[blank_index]
            
            elif direction == "G":
                # on permute la position du trou avec la tuile à gauche
                tiles[blank_index], tiles[x-1+y*self.__width] = tiles[x-1+y*self.__width], tiles[blank_index]
            
            else: # Comme on vérifie déjà les positions possibles alors forcément ce sera la droite ici
                tiles[blank_index], tiles[x+1+y*self.__width] = tiles[x+1+y*self.__width], tiles[blank_index]
    
    def save_undo(self, direction) -> None:
        """
        Description : Méthode qui met en mémoire la direction passé en paramètre
        Param : direction (str) 
        """
        self.__movement.empiler(direction) 
        
    
    def undo(self) -> None:
        """
        Description : Méthode qui permet d'annuler le coup précédent
        """
        undo_dict = {"H":"B", "B":"H", "D":"G", "G":"D"}
        if not self.__movement.est_vide():
            move = undo_dict[self.__movement.depiler()]
            self.move_blank_to(move)
        else:
            print("Aucun coup enregistré")
    
    def random_puzzleV1(self) -> None:
        """
        Description : Méthode qui génére un puzzle aléatoire
        """
        for _ in range(20):
            self.move_blank_to(choice(self.enum_direction()))
    
    def play(self) -> None:
        """
        Description : Méthode qui permet de jouer au puzzle
        """
        self.random_puzzleV1()
        while not self.is_finish():
            self.display()
            usr_input = "404"
            while usr_input not in self.enum_direction() + ["A", "R"]:
                usr_input = input("Votre coup? ((H)aut, (B)as, (G)auche, (D)roit, (A)bandon, (R)etour) ").upper()
            
            if usr_input == "A":
                print("Avec un peu de perśev́erance vous auriez pu trouver")
                print("Chargement de la solution ...")
                print(self.solve())
                return None
            
            elif usr_input == "R":
                self.undo()
            
            else:
                self.move_blank_to(usr_input)
                self.save_undo(usr_input)
        
        
        self.display()
        print("Vous avez réussi le puzzle !!")

        
    def random_puzzleV2(self) -> None:
        shuffle(self.__tiles)
            
    def neighbour_list(self) -> list:
        neighbour = []
            
        for direction in self.enum_direction():
            P = Puzzle(self.__tiles[:])
            P.move_blank_to(direction)
            neighbour.append(P)
                
                
        return neighbour
        
    def build_solution(self, current, seen):
        path = [current] # puzzles
        puzzle = current
        while puzzle != None:
            puzzle = seen[puzzle]
            path.append(puzzle)
        
        #for puzzle in reversed(path):
        #    puzzle.display()
        path = list(reversed(path[:-1]))
        return Puzzle.get_command_from_config(path)
        #return path
    
    def solve(self):
        candidates = [self]
        seen = {self:None}
        found = False    
        debut = time()
        while candidates != [] and found != True:
            current = candidates.pop(Puzzle.best_config_id(candidates))
            if current.is_finish():
                found = True
            
            else:
                for neighbour in current.neighbour_list():
                    if neighbour not in seen:
                        seen[neighbour] = current
                        candidates.append(neighbour)
        if found:
            fin = time()
            print("Solution trouvée")
            print("Nombre de puzzle testé : " + str(len(seen)))
            print("En " + str(round(fin-debut,3)) + " secondes")
            return self.build_solution(current, seen)
        else:
            raise ImpossiblePuzzleError("Can't solve this puzzle")
    
    @staticmethod
    def best_config_id(list_config):
        if list_config != []:
            best_index = 0 # Postulat que l'indice 0 correspond à l'indice de la meilleure configuration
            for i in range(1,len(list_config)): # Pour toutes les autres configuration
                if list_config[i].tiles_well_placed() > list_config[best_index].tiles_well_placed(): # Si on trouve une meilleure configuration
                    best_index = i # Alors son indice devient l'indice de la meilleure configuration
            return best_index
        
        raise Exception("No index in empty list")
        
    @staticmethod    
    def get_command_from_config(list_config):
        list_command = []
        if list_config != []:
            width = list_config[0].get_width()
            for i in range(len(list_config)-1):
                prev_puzzle = list_config[i]
                next_puzzle = list_config[i+1]
                
                # position du trou de l'ancien puzzle
                prev_index = prev_puzzle.get_blank()
                prev_pos = (prev_index % width, prev_index // width)
                
                # position du trou du puzzle suivant
                next_index = next_puzzle.get_blank()
                next_pos = (next_index % width, next_index // width)
                
                if prev_pos[0] == next_pos[0]:
                    # Cas ou la colonne n'a pas changé
                    if next_pos[1] > prev_pos[1]:
                        # Si la colonne à la position suivante est plus grande alors c'est un déplacement vers le bas
                        list_command.append("B")
                    else:
                        #Sinon c'est forcément un déplacement vers le haut
                        list_command.append("H")
                else:
                    # Cas ou la ligne n'a pas changé
                    if next_pos[0] > prev_pos[0]:
                        # Si la colonne suivante est plus grande alors c'est un déplacement vers la droite
                        list_command.append("D")
                    else:
                        #Sinon c'est forcément un déplacement vers la gauche
                        list_command.append("G")
        return list_command
                        
                    
                    
taille = 3*3
list_tiles = [Tile(i+1) for i in range(taille-1)] + [Tile()]

situation1 = [Tile(),Tile("1"),Tile("3"),Tile("4"),
              Tile("5"),Tile("2"),Tile("7"),Tile("10"),
              Tile("9"),Tile("8"),Tile("6"),Tile("11"),
              Tile("13"),Tile("14"),Tile("15"),Tile("12")]


jeu = Puzzle(situation1)
jeu.display()
print(jeu.solve())