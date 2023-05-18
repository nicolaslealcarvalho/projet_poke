class Status:

    """
    this class alow to change the status of a Chocobo

    Exemple:
    >>> sta = Status()
    >>> sta.getPourcDegat()
    0
    >>> sta.getNbTourLeft()
    0
    >>> sta.getPassTurn()
    False
    >>> sta.nextTurn()
    >>> sta.getNbTourLeft()
    -1
    """

    def __init__(self):
        self.nbTours = 0
        self.infligeDeg = 0
        self.passTours = False
        self.changStat = [(0,0,0,0),(0,0,0,0)]

    def getPourcDegat(self):
        """
        this method return the pourcentage of dammage that the Chocobos will take

        Return: a int representing dammage that the chocobo will take

        Exemple:
        >>> sta = Status()
        >>> sta.getPourcDegat()
        0
        """
        return self.infligeDeg

    def getNbTourLeft (self):
        """
        this method return the number of turn that status will be inflict to the Chocobos

        Return: a int representing time the Chocobo has to suffer of his status

        Exemple:
        >>> sta = Status()
        >>> sta.getNbTourLeft()
        0
        """
        return self.nbTours
    
    def getPassTurn(self):
        """
        this method return if the Chocobas has to pass his turn during the Status

        Return: True if he has to, False otherwise

        Exemple:
        >>> sta = Status()
        >>> sta.getPassTurn()
        False
        """
        return self.passTours

    def nextTurn(self):
        """
        this method change the number of turn that the status will be inflicted

        Exemple:
        >>> sta = Status()
        >>> sta.nextTurn()
        False
        """
        self.nbTours -= 1
        if self.nbTours <= 0 :
            return False
