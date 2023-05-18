from Toir.Shocobos.Type import Type
from Toir.Shocobos.Capacite.abstract_capacite import *
from doctest import *

class aquaFlowAbility(AbstractAbility):
    """
    this class is use to represent the ability aqua flow

    Exemple:
    >>> ability = aquaFlowAbility()
    >>> chocobAllier = Chocobos()
    >>> chocobEnemis = Chocobos()
    >>> ability.getName()
    'Aqua Flow'
    >>> ability.getType().getNomType()
    'eau'
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
        self.name = 'Aqua Flow'
        self.type = Type("eau")
        self.category = "SPECIAL"
        self.power = 60
        self.accuracy = 100 
