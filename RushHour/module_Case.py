## Grando Lukas
## Module Case

import string
from module_exceptions import BadCellContentError

class Case:
    
    def __init__(self, content = " ") -> None:
        if len(content) != 1:
            raise BadCellContentError("Cell content must be a space/uppercase letter not " + str(content))
        
        self.__content = str(content).upper()
        
    
    def get_content(self) -> str:
        return self.__content
    
    
    def set_content(self, new_content) -> None:
        self.__content = new_content
        
    def is_blank(self) -> bool:
        """
        Description : Prédicat qui retourne vrai si la case est vide
        """
        return self.__content == " "
    
    def is_car(self) -> bool:
        """
        Description : Prédicat qui retourne vrai si la case est un véhicule
        """
        return self.__content in string.ascii_uppercase

    def clear(self) -> None:
        """
        Description : Méthode qui vide la case
        """
        self.__content = " "
        
    
        
        
    
    
        
        
    
        
        