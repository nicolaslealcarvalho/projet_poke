from Toir.Shocobos.Status.Status import *

class Status_Lethargie(Status):

    """
    this class alow to describe the status Lethargie of a Chocobo

    Exemple:
    >>> sta = Status_Lethargie()
    >>> sta.getPourcDegat()
    0
    >>> sta.getNbTourLeft()
    3
    >>> sta.getPassTurn()
    True
    """

    def __init__(self):
        self.nbTours = 3
        self.infligeDeg = 0
        self.passTours = True
        self.changStat = [(0,0,0,0),(0,0,0,0)]
