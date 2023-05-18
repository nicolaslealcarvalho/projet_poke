from Toir.Shocobos.Type import Type
from Toir.Shocobos.Capacite.abstract_capacite import *
from doctest import *

class electaserAbility(AbstractAbility):
    """
    this class is use to represent the ability Electaser

    Exemple:
    >>> ability = electaserAbility()
    >>> chocobAllier = Chocobos()
    >>> chocobEnemis = Chocobos()
    >>> ability.getName()
    'Electaser'
    >>> ability.getType().getNomType()
    'electrique'
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
        self.name = 'Electaser'
        self.type = Type("electrique")
        self.category = "SPECIAL"
        self.power = 60
        self.accuracy = 100 