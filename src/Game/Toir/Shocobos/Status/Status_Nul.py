from Toir.Shocobos.Status.Status import *

class Status_Nul(Status):

    """
    this class alow to describe the status of a Chocobo

    Exemple:
    >>> sta = Status_Nul()
    >>> sta.getPourcDegat()
    0
    >>> sta.getNbTourLeft()
    -1
    >>> sta.getPassTurn()
    False
    """

    def __init__(self):
        self.nbTours = -1
        self.infligeDeg = 0
        self.passTours = False
        self.changStat = [(0,0,0,0),(0,0,0,0)]
