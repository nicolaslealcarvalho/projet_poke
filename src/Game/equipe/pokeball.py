from equipe import *
from Toir.Shocobos.Chocobos import *
from random import *

class Pokeball:
    
    """
    this class allows the user to use a pokeball 

    Parameter: the team of the user
               the pokemon that will maybe be catch

    Exemple:
    >>> eq = Equipe()
    >>> randomChocobo = Chocobos()
    >>> Pokeball(eq,randomChocobo)
    >>> a = eq.get4Pokemon()
    """

    def __init__(self,equ,pokemonACapturer):
        nbAlea = randint(0, 100)
        if nbAlea >= 50:
            equ.ajoutPokemon(pokemonACapturer)
