#Grando Lukas TD08

from random import shuffle
#from time import sleep

class Carte:
    '''represente une carte a jouer'''
 
    def __init__(self, valeur, couleur) -> None:
        '''(Carte,str,str)->None       
        initialise la valeur et la couleur de la carte'''
        self.valeur = valeur
        self.couleur = couleur  # "pique", "coeur", "trefle" ou "carreau"
 
    def __repr__(self) -> str:
        '''(Carte)->str
        retourne une representation de l'objet'''
        return self.valeur + self.couleur
 
    def __eq__(self, autre) -> bool:
        '''(Carte,Carte)->bool
        self == autre si la valeur et la couleur sont les memes'''
        
        if type(autre) == Carte: #ou if isinstance(autre, Carte):
            return (self.valeur, self.couleur) == (autre.get_valeur(), autre.get_couleur())
        
        return False
    
    def get_valeur(self) -> str:
        '''Retourne SEULEMENT la valeur de la carte.'''
        return self.valeur
    
    def get_couleur(self) -> str:
        '''Retourne SEULEMENT la valeur de la carte.'''
        return self.couleur
 
 
 
class JeuDeCartes:
    '''represente une jeu de 52 cartes'''
    # valeurs et couleurs sont des variables de classe
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    
    couleurs= [chr(9824),chr(9825),chr(9826),chr(9827)]# symboles de : pique, coeur, carreau, trèfle
     
    def __init__(self) -> None:
        'initialise le paquet de 52 cartes'
        self.paquet = []          # paquet vide au debut
        for couleur in JeuDeCartes.couleurs:
            for valeur in JeuDeCartes.valeurs: # variables de classe
                # ajoute une Carte de valeur et couleur
                self.paquet.append(Carte(valeur, couleur))
        #à la fin du constructeur, paquet est un attribut de la classe JeuDeCartes 
    
    def __iter__(self) -> 'list_iterator':
        '''Description : Notre jeu de carte devient un itérable'''
        return self.paquet.__iter__()
    
    def __len__(self):
        '''correspond à la longueur de notre objet JeuDeCartes'''
        return len(self.paquet)
    
    def get_paquet(self) -> list:
        '''accesseur de paquet'''
        return self.paquet
    
    def tireCarte(self) -> Carte:
        '''(JeuDeCartes)->Carte
        distribue une carte, la premiere du paquet'''
        if self.paquet == []:
            raise Exception("Paquet de carte vide")
        
        return self.paquet.pop(0)
 
    def battre(self) -> None:
        '''(JeuDeCartes)->None
        pour battre le jeu des cartes'''
        shuffle(self.paquet)
    
    def __repr__(self) -> str:
        '''retourne une representation de l'objet'''
        return 'Paquet('+str(self.paquet)+')'
 
    def __eq__(self, autre) -> bool:
        '''retourne True si les paquets ont les meme cartes
           dans le meme ordre'''
        if type(autre) == JeuDeCartes:
            return self.paquet == autre.get_paquet()
        
        return False
            
    
    
class Main():
    '''represente une main des cartes a jouer'''
 
    def __init__(self, joueur) -> None:
        '''(Main, str)-> none
        initialise le nom du joueur et la liste de cartes avec liste vide'''
        self.joueur = joueur
        self.main = []
        
    def ajouteCarte(self, Carte) -> None:
        '''(Main, Carte) -> None
        ajoute une carte a la main'''
        self.main.append(Carte)
        
    def remporte_le_pli(self,Pli) -> None:
        '''(Main, pli)->Carte
        toutes les cartes de la liste pli sont ajoutees a la main
        pli est une liste de Cartes
        '''
        for Carte in Pli:
            self.ajouteCarte(Carte)
            
    def tireCarte(self) -> Carte:
        '''(Main)->Carte
        distribue une carte, la premiere/dernière du paquet'''
        if self.main == []:
            raise Exception("Main de " + self.joueur + " est vide")
        return self.main.pop(0)


    def montreMain(self) -> None:
        '''(Main)-> None
        affiche le nom du joueur et la main'''
        return print(self.joueur,':\n',self.main)
    
    def get_name(self) -> str:
        '''(Main)-> None
        affiche le nom du joueur et la main'''
        return self.joueur
    
    def get_main(self) -> list:
        '''accesseur de l'attribut main'''
        return self.main
    
    def __eq__(self, autre) -> bool:
        '''retourne True si les main ont les meme cartes
           dans la meme ordre'''
        if type(autre) == Main:
            return self.main == autre.get_main()
        
        return False
    
    def __len__(self) -> int:
        '''longueur de l'objet main'''
        return len(self.main)
 
    def __repr__(self) -> str:
        '''retourne une representation de l'objet'''
        return self.joueur + " : " + str(self.main)
    


class Bataille:
    '''le jeu de bataille'''
    
    valeurs = {JeuDeCartes.valeurs[i]:i+2 for i in range(len(JeuDeCartes.valeurs))}
    NB_PLI_MAX = 3000 # On considère qu'après 3000 coups, la partie est infini
                      # il serait intéressant d'étudier quand est-ce qu'une partie est réellement infini (je n'ai pas eu le temps)
    def __init__(self, joueur1, joueur2):
        #paquet de carte qu'on mélange
        self.paquet = JeuDeCartes()
        self.paquet.battre()
        
        #La main des joueurs qu'on rempli avec la moitié des cartes du jeu
        self.joueur1 = Main(joueur1)
        self.joueur1.remporte_le_pli([self.paquet.tireCarte() for i in range(26)])
        
        self.joueur2 = Main(joueur2)
        self.joueur2.remporte_le_pli([self.paquet.tireCarte() for i in range(26)])
        
    def __repr__(self) -> str:
        '''retourne une representation de l'objet'''
        return self.joueur1.get_name() + " vs " + self.joueur2.get_name()
    
    def est_fini(self) -> bool:
        """
        Description : Prédicat qui retourne true si la bataille est terminé ! (càd si un joueur n'a plus de carte)
        """
        return len(self.joueur1) == 0 or len(self.joueur2) == 0
    
    def pli(self, pli_precedant = None) -> None:
        """
        Description : Déroulement d'un pli
        Params : pli_precedant (str), les cartes à gagner du pli précédant : en cas de bataille  
        """
        
        #Les 2 joueurs tirent une carte de leur main
        carte_1, carte_2 = self.joueur1.tireCarte(), self.joueur2.tireCarte()
        
        if pli_precedant is None: # une liste peut muter même lorsqu'elle est en valeur par défaut
            pli_precedant = []    # il vaut mieux mettre une valeur absurde ou None pour ensuite utiliser une liste vide
        
        #on annonce les cartes tirés
        print(self.joueur1.get_name() + " : " + str(carte_1) + " | " + self.joueur2.get_name() + " : " + str(carte_2))
        
        #Cas ou le joueurs 1 remporte le pli
        if Bataille.valeurs[carte_1.get_valeur()] > Bataille.valeurs[carte_2.get_valeur()]:
            print(self.joueur1.get_name() + " remporte le pli !")
            self.joueur1.remporte_le_pli([carte_1,carte_2] + pli_precedant) # il gagne les carte du pli actuel + ceux du pli précédant
        
        #Cas ou il y a une bataille
        elif Bataille.valeurs[carte_1.get_valeur()] == Bataille.valeurs[carte_2.get_valeur()]:
            print("Bataille ! Les 2 joueurs pose une carte face caché")
            
            if len(self.joueur1) > 1 and len(self.joueur2) > 1: # Si les deux ont encore des cartes (au moins 2)
                # On lance le pli suivant avec les cartes actuels en gain + 2 cartes faces cachées
                self.pli([carte_1, carte_2, self.joueur1.tireCarte(), self.joueur2.tireCarte()])
            else:
                print("Un joueur n'a plus de carte, fin de la partie") # Si un joueur n'a plus assez de carte pour une bataille alors il a forcement perdu 
        
        #Cas ou le joueur 2 remporte le pli
        else:
            print(self.joueur2.get_name() + " remporte le pli !")
            self.joueur2.remporte_le_pli([carte_1,carte_2] + pli_precedant)
            
    
    def joue(self) -> None:
        '''joue une partie'''
        coup = 0
        while not(self.est_fini()): # boucle de jeu 
            self.pli()
            coup += 1
            #sleep(0.5) finalement une partie est assez longue
            
            if coup >= Bataille.NB_PLI_MAX: # Pour éviter une boucle while sans fin
                print()
                print("La partie semble infini ! Fin du jeu !")
                
                while len(self.joueur1) == len(self.joueur2): # On accepte aucune égalité
                    print("ÉGALITÉ ! On relance un pli")
                    self.pli()
                
                if len(self.joueur1) > len(self.joueur2):
                    print(self.joueur1.get_name() + " est le vainqueur !")
                
                else:
                    print(self.joueur2.get_name() + " est le vainqueur !")
                
                return None # On renvoit rien pour casser la boucle et la méthode  
        
        print()
            
        if len(self.joueur1.get_main()) != 0:
            print(self.joueur1.get_name() + " est le vainqueur !")
            
        else:
            print(self.joueur2.get_name() + " est le vainqueur !")
            
    
    def rejouer(self) -> None:
        """
        Description : Permet de rejouer une partie de bataille avec les mêmes joueurs. Cette fonction comprends
        """
        self.__init__(self.joueur1.get_name(), self.joueur2.get_name()) # Comme on réinitialise tout nos attribut autant appeler directement notre constructeur 
        self.joue()
            


if __name__ == "__main__":
    plr_1 = "Napoléon I"
    plr_2 =  "Alexandre I"
    concours = Bataille(plr_1, plr_2)
    print(concours)
    input("Lancement d'une partie (Appuyez sur une touche) ")
    concours.joue()
    