class Effet :

    """
    this class allow to manipulate various effect(stat boost or down)
    """

    def __init__(self, atk = 0, Def = 0, atkSpe = 0 , defSpe = 0 ,matrice= [(0,0,0,0),(0,0,0,0)]):
        if matrice == [(0,0,0,0),(0,0,0,0)]:
            self.Atk = atk
            self.Def = Def
            self.AtkSpe = atkSpe
            self.DefSpe = defSpe
        else:
            self.Atk = (matrice[0][0]) - (matrice[1][0])
            self.Def = (matrice[0][1]) - (matrice[1][1])
            self.AtkSpe = (matrice[0][2]) - (matrice[1][2])
            self.DefSpe = (matrice[0][3]) - (matrice[1][3])
    
    def changement(self,listeChang):
        """
        this method allow to change effect with a matrice of change

        Exemple:
        >>> test = Effet([(1,0,1,0), (0,1,0,1)])
        >>> test.changement([(1,0,1,0), (0,1,0,1)])
        >>> test.getAtk()
        1
        >>> test.getDef()
        -1
        >>> test.getAtkSpe()
        1
        >>> test.getDefSpe()
        -1 
        """
        self.Atk = listeChang[0][0] - listeChang[1][0]
        self.Def = listeChang[0][1] - listeChang[1][1]
        self.AtkSpe = listeChang[0][2] - listeChang[1][2]
        self.DefSpe = listeChang[0][3] - listeChang[1][3]

    def getAtk(self):
        """
        this method allow to get the Atk of the Chocobo
        
        Return: the atk of the Chocobo

        >>> test = Effet()
        >>> test.getAtk()
        0
        """
        return self.Atk

    def getDef(self):
        """
        this method allow to get the def of the Chocobo
        
        Return: the def of the Chocobo

        >>> test = Effet()
        >>> test.getDef()
        0
        """
        return self.Def

    def getAtkSpe(self):
        """
        this method allow to get the AtkSpe of the Chocobo
        
        Return: the atkSpe of the Chocobo

        >>> test = Effet()
        >>> test.getAtkSpe()
        0
        """
        return self.AtkSpe

    def getDefSpe(self):
        """
        this method allow to get the DefSpe of the Chocobo
        
        Return: the DefSpe of the Chocobo

        >>> test = Effet()
        >>> test.getDefSpe()
        0
        """
        return self.DefSpe
    
    def getMatrice(self):
        """
        this method allow to get the matrice of the Chocobo
        
        Return: the matrice of the Chocobo

        >>> test = Effet()
        >>> test.getMatrice()
        [(0,0,0,0),(0,0,0,0)]
        """
        l = [[None,None,None,None],[None,None,None,None]]
        if self.Atk >= 0:
            l[0][0]= self.Atk
            l[1][0]= 0
        else:
            l[1][0]= -self.Atk
            l[0][0]= 0
        if self.Def >= 0:
            l[0][1]= self.Def
            l[1][1]= 0
        else:
            l[1][1]= -self.Def
            l[0][1]= 0
        if self.AtkSpe >= 0:
            l[0][2]= self.AtkSpe
            l[1][2]= 0
        else:
            l[1][2]= -self.AtkSpe
            l[0][2]= 0
        if self.DefSpe >= 0:
            l[0][3]= self.DefSpe
            l[1][3]= 0
        else:
            l[1][3]= -self.DefSpe
            l[0][3]= 0
        matrice = [tuple(l[0]),tuple(l[1])]
        return matrice
