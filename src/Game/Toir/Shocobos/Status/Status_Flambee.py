from Toir.Shocobos.Status.Status import *

class Status_Flambee(Status):

    """
    this class alow to describe the status flambee of a Chocobo

    Exemple:
    >>> sta = Status_Flambee()
    >>> sta.getPourcDegat()
    8
    >>> sta.getNbTourLeft()
    4
    >>> sta.getPassTurn()
    False
    """

    def __init__(self):
        self.nbTours = 4
        self.infligeDeg = 8
        self.passTours = False
        self.changStat = [(0,0,0,0),(2,0,0,0)]
