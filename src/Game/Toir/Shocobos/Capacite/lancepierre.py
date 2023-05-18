from Toir.Shocobos.Type import Type
from Toir.Shocobos.Capacite.abstract_capacite import *
from doctest import *

class LancepierreAbility(AbstractAbility):
    """
    this class is use to represent the ability Lance Pierre

    Exemple:
    >>> ability = LancepierreAbility()
    >>> chocobAllier = Chocobos()
    >>> chocobEnemis = Chocobos()
    >>> ability.getName()
    'Lance Pierre'
    >>> ability.getType().getNomType()
    'sol'
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
        self.name = 'Lance Pierre'
        self.type = Type("sol")
        self.category = "PHYSICAL"
        self.power = 20
        self.accuracy = 100 