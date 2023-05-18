from Toir.Shocobos.EnumType import *

class Type:
    """
    cette classe permet d'instancier le type d'un pokemon ou d'une capaciter

    Exemple:
    >>> ty = Type('feu')
    >>> ty.avantage()
    [EnumType.plante]
    >>> ty.desavantage()
    [EnumType.feu, EnumType.eau]
    """

    def __init__(self,nomType):
        typeCreer = EnumType(nomType)
        if typeCreer in EnumType:
            self.nomType = nomType
            self.typeCreer = typeCreer
            

    def avantage(self):
        """
        cette methode permet de connaitre les different avantage que le type choisit a sur les autres

        Exemples:
        >>> ty = Type('feu')
        >>> ty.avantage()
        [EnumType.plante]
        """

        if self.typeCreer == EnumType.feu:
            return [EnumType.plante]
        elif self.typeCreer == EnumType.eau:
            return [EnumType.feu, EnumType.sol]
        elif self.typeCreer == EnumType.plante:
            return [EnumType.eau, EnumType.sol]
        elif self.typeCreer == EnumType.electrique:
            return [EnumType.eau, EnumType.vol]
        elif self.typeCreer == EnumType.sol:
            return [EnumType.electrique, EnumType.feu]
        elif self.typeCreer == EnumType.vol:
            return [EnumType.plante]
        elif self.typeCreer == EnumType.normal:
            return []
        elif self.typeCreer == EnumType.combat:
            return [EnumType.normal]
        elif self.typeCreer == EnumType.psy:
            return [EnumType.combat]
        else:
            return []



    def desavantage(self):
        """
        cette methode permet de connaitre les different desavantage que le type choisit a sur les autres

        Exemples:
        >>> ty = Type('feu')
        >>> ty.desavantage()
        [EnumType.feu, EnumType.eau]
        """

        if self.typeCreer == EnumType.feu:
            return [EnumType.feu, EnumType.eau]
        elif self.typeCreer == EnumType.eau:
            return [EnumType.eau, EnumType.plante]
        elif self.typeCreer == EnumType.plante:
            return [EnumType.plante, EnumType.feu]
        elif self.typeCreer == EnumType.electrique:
            return [EnumType.electrique, EnumType.sol]
        elif self.typeCreer == EnumType.sol:
            return [EnumType.sol, EnumType.vol]
        elif self.typeCreer == EnumType.vol:
            return [EnumType.electrique, EnumType.vol]
        else:
            []

    def getNomType(self):
        return self.nomType

