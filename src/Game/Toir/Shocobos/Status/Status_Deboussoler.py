from Toir.Shocobos.Status.Status import *

class Status_Deboussoler(Status):

    """
    this class alow to describe the status Deboussoler of a Chocobo

    Exemple:
    >>> sta = Status_Deboussoler()
    >>> sta.getPourcDegat()
    20
    >>> sta.getNbTourLeft()
    1
    >>> sta.getPassTurn()
    True
    """

    def __init__(self):
        self.nbTours = 1
        self.infligeDeg = 20
        self.passTours = True
        self.changStat = [(0,0,0,0),(0,0,0,0)]
