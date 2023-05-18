from Toir.Shocobos.Type import Type
from Toir.Shocobos.Capacite.abstract_capacite import *
from doctest import *

class ChauffeAbility(AbstractAbility):
    """
    this class is use to represent the ability chauffe

    Exemple:
    >>> ability = ChauffeAbility()
    >>> chocobAllier = Chocobos()
    >>> chocobEnemis = Chocobos()
    >>> ability.getName()
    'chauffe'
    >>> ability.getType().getNomType()
    'feu'
    >>> ability.getCategory()
    "SPECIAL"
    >>> ability.getPower()
    60
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
        self.name = 'chauffe'
        self.type = Type("feu")
        self.category = "SPECIAL"
        self.power = 60
        self.accuracy = 100 

