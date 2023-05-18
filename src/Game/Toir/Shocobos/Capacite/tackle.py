from Toir.Shocobos.Type import Type
from Toir.Shocobos.Capacite.abstract_capacite import *
from doctest import *

class TackleAbility(AbstractAbility):
    """
    this class is use to represent the ability tackle

    Exemple:
    >>> ability = TackleAbility()
    >>> chocobAllier = Chocobos()
    >>> chocobEnemis = Chocobos()
    >>> ability.getName()
    'tackle'
    >>> ability.getType().getNomType()
    'vol'
    >>> ability.getCategory()
    "PHYSICAL"
    >>> ability.getPower()
    20
    >>> ability.getAccuracy()
    100
    >>> ability.setReceiver(chocobEnemis)
    >>> ability.setLauncher(chocobAllier)
    >>> ability.applique()
    >>> ability.getDegats() != 0
    True
    """
    def __init__(self):
        super().__init__()
        self.name = 'tackle'
        self.type = Type("vol")
        self.category = "PHYSICAL"
        self.power = 20
        self.accuracy = 100 
