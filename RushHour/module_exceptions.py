## Grando Lukas
##  Fichier contenant les éventuelles erreurs dues à une mauvaise manipulation par l'utilisateur

class VehiculeError(Exception):
    """Erreur relative à la classe Vehicule"""

class LevelsDirectoryError(Exception):
    """Lorsque le dossier niveau est vide"""

class BadLevelFileError(Exception):
    """Les infomartions dans un fichiers niveau sont invalides"""
    
class BadCellContentError(Exception):
    """Contenu de case invalide"""
    
