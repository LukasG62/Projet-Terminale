## Grando Lukas
## Tuile POO

class Tile:
    def __init__(self, value = " ") -> None:
        self.__value = str(value)
    
    
    def get_value(self) -> str:
        return self.__value
    
    def is_blank(self) -> bool:
        """
        Description : Prédicat qui retourne vrai si la tuile est le trou
        """
        return self.get_value() == " "
    
    def display_number(self) -> None:
        """
        Description : Affiche la valeur de la tuile
        """
        print(self.get_value())
