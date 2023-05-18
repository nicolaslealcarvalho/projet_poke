from random import *
from Toir.Shocobos.Type import *
from Toir.Shocobos.Status.Status_Nul import *
from Toir.Shocobos.Chocobos import *
from Toir.Shocobos.Status.Effet import *
from math import *



PHYSICAL = "PHYSICAL"
SPECIAL = "SPECIAL"
STATUS = "STATUS"

TARGET_SELF = 0
TARGET_ENEMY = 1

CATEGORYS: list[str] = [PHYSICAL, SPECIAL, STATUS]

class AbstractAbility(object):
    """
    this class is use to create every ability use in this game

    Exemple:
    >>> ability = AbstractAbility()
    >>> chocobAllier = Chocobos()
    >>> chocobEnemis = Chocobos()
    >>> ability.getName()
    False
    >>> ability.getType()
    False
    >>> ability.getCategory()
    False
    >>> ability.getPower()
    False
    >>> ability.getAccuracy()
    False
    >>> ability.setReceiver(chocobEnemis)
    >>> ability.setLauncher(chocobAllier)
    >>> ability.getDegats()
    0    
    """
    def __init__(self, launcher = False, receiver = False ):
        self.name = False
        self.type = False
        self.category = False
        self.power = False
        self.accuracy = False
        self.status = Status_Nul()
        self.boost = Effet()
        self.des = Effet()

        self.degats = 0

        self.launcher = launcher
        self.receiver = receiver
    
    def getName(self):
        """
        this class is use to create every ability use in this game

        Exemple:
        >>> ability = AbstractAbility()
        >>> ability.getName()
        False
        """
        return self.name
    
    def getType(self):
        """
        this method return the type of the capacity

        Exemple:
        >>> ability = AbstractAbility()
        >>> ability.getType()
        False
        """
        return self.type

    def getCategory(self):
        """
        this method return the category of the capacity (SPECIAL,PHYSIQUE)

        Exemple:
        >>> ability = AbstractAbility()
        >>> ability.getCategory()
        False
        """
        return self.category
    
    def getPower(self):
        """
        this method return the power of the used ability

        Exemple:
        >>> ability = AbstractAbility()
        >>> ability.getPower()
        False
        """
        return self.power
    
    def getAccuracy(self):
        """
        this method return the accuracy of the used ability

        Exemple:
        >>> ability = AbstractAbility()
        >>> ability.getAccuracy()
        False
        """
        return self.accuracy
    
    def setReceiver(self,receiver):
        """
        this method set the pokemon that will receive the ability

        Exemple:
        >>> ability = AbstractAbility()
        >>> chocobEnemis = Chocobos()
        >>> ability.setReceiver(chocobEnemis)
        >>> ability.receiver == chocobEnemis
        True
        """
        self.receiver = receiver

    def setLauncher(self,launcher):
        """
        this method set the pokemon that will launch the ability

        Exemple:
        >>> ability = AbstractAbility()
        >>> chocoboAllier = Chocobos()
        >>> ability.setLauncher(chocoboAllier)
        >>> ability.launcher == chocoboAllier
        True
        """
        self.launcher = launcher

    def getStatus(self):
        """
        this method return the status that the capacity will inflict

        Exemple:
        >>> ability = AbstractAbility()
        >>> isinstance(ability.getStatus(),Status_Nul)
        True
        """
        return self.status
    
    def getBoost(self):
        """
        this method return the boost that the capacity will give to the user

        Exemple:
        >>> ability = AbstractAbility()
        >>> isinstance(ability.getBoost(),Effet)
        True
        """
        return self.boost
    
    def getDes(self):
        """
        this method return the des that the capacity will inflict to the opponent

        Exemple:
        >>> ability = AbstractAbility()
        >>> isinstance(ability.getDes(),Effet)
        True
        """
        return self.des

    def applique(self):
        """
        this method will apply the ability to the oponent chocobos with the statistique,buf,etc from the ally

        Exemple:
        >>> ability = AbstractAbility()
        >>> chocobAllier = Chocobos()
        >>> chocobEnemis = Chocobos()
        >>> ability.setReceiver(chocobEnemis)
        >>> ability.setLauncher(chocobAllier)
        >>> ability.applique()
        >>> ability.degats == 0
        """
        if self.name != False :
            if randint(0,100) <= self.accuracy:
                if self.category == "PHYSICAL":
                    degat = (self.power * self.launcher.getChocobos().getAtt())// self.receiver.getChocobos().getDef()
                elif self.category == "SPECIAL":
                    degat = (self.power * self.launcher.getChocobos().getAttSpe())// self.receiver.getChocobos().getDefSpe()

                if self.receiver in self.type.avantage():
                    degat = 2 * degat
                if self.receiver in self.type.desavantage():
                    degat =  degat // 2
                self.receiver.changePV((degat)) # plus besoin du ceil, renvoie tout en int
                self.degats = degat
                print(self.degats)

    def getDegats(self):
        """
        this method return the damage that will be inflict to the opponent chocobo

        Exemple:
        >>> ability = AbstractAbility()
        >>> ability.getDegats()
        0
        """
        return self.degats

