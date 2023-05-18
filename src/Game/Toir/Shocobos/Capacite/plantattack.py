from Toir.Shocobos.Type import Type
from Toir.Shocobos.Capacite.abstract_capacite import *

class PlantattackAbility(AbstractAbility):
    """
    this class is use to represent the ability Plantattack

    Exemple:
    >>> ability = PlantattackAbility()
    >>> chocobAllier = Chocobos()
    >>> chocobEnemis = Chocobos()
    >>> ability.getName()
    'Plantattack'
    >>> ability.getType().getNomType()
    'plante'
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
        self.name = 'Plantattack'
        self.type = Type("plante")
        self.category = "PHYSICAL"
        self.power = 20
        self.accuracy = 100 
