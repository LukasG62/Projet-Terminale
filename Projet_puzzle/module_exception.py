## Grando Lukas
## POO héritant de la super classe python Exception

class MovementError(Exception):
    """Movement cannot be done"""

class DimensionError(Exception):
    """Invalid number of tiles (Puzzle must be a square)"""
    
class ImpossiblePuzzleError(Exception):
    """Generated puzzle cannot be solved"""