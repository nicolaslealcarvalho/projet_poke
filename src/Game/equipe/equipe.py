import copy
import json
from Toir.Shocobos.Chocobos import *

class Equipe:
    """
    this class allow to represent the team of the player

    Exemple:
    >>> eq = Equipe()
    >>> pok1 = eq.get1Pokemon()
    >>> isisntance(eq.get1Pokemon(),Chocobos)
    True
    >>> isisntance(eq.get2Pokemon(),Chocobos)
    True
    >>> isisntance(eq.get3Pokemon(),Chocobos)
    True
    >>> eq.get4Pokemon()
    False
    >>> eq.get5Pokemon()
    False
    >>> eq.get6Pokemon()
    False
    >>> print(eq.getnbPokemon(0) == eq.get1Pokemon())
    True
    >>> eq.taille()
    2
    >>> eq.changementPokemon(2)
    >>> eq.get1Pokemon() == poke1
    True
    >>> randomChoco = Chocobos()
    >>> eq.ajoutPokemon(randomChoco)
    >>> eq.get4Pokemon() == randomChoco
    True
    """

    def __init__(self):

        self.equipePokemon = list()

        with open('src/Game/equipe/equipe.json') as mon_fichier:
            data = json.load(mon_fichier)

        for i in data:

            pokemon = Chocobos()
            pokemon.getChocobos().generateFromJson(i)
            self.equipePokemon.append(pokemon)
    
    def getPokemon(self,nb):
        """
        this method allow to take any Chocobos of the team

        Parameter: the place of the choose Chocobo

        Return: the Chocobos at the place choose or False if the team dosen't have enough Chocobos

        Exemple:
        >>> eq = Equipe()
        >>> eq.get6Pokemon()
        False
        """
        if self.taille() >= nb:
            return self.equipePokemon[nb]
        else:
            return False
        
    def taille(self):
        """
        this method return the length of the team (minus 1 for coding purpose)

        Return: the length of the team

        Exemple:
        >>> eq = Equipe()
        >>> eq.taille()
        2
        """
        return len(self.equipePokemon) - 1


    def changementPokemon(self,num):
        """
        this methode swap betwen the first Chocobo and the choose one

        Exemple:
        >>> eq = Equipe()
        >>> Choco3 = eq.get3Pokemon()
        >>> eq.changementPokemon(2)
        >>> eq.get1Pokemon() == Choco3
        True  
        """
        self.equipePokemon[0], self.equipePokemon[num - 1] = self.equipePokemon[num - 1], self.equipePokemon[0]

    def ajoutPokemon(self,poke):
        """
        this methode add a new Chocobos to the team or ,if it cannot, return False
        
        Parameter: poke that will be the Chocobos that will be added

        Return: False if you cannot add the Chocobos

        Exemple:
        >>> randomChoco = Chocobos()
        >>> eq = Equipe()
        >>> eq.ajoutPokemon(randomChoco)
        >>> eq.get4Pokemon() == randomChoco
        True
        """
        if len(self.equipePokemon) >= 6:
            return False
        else:
            self.equipePokemon.append(copy.copy(poke))


    def save(self):
        """
        this method allow to save the stat of the team in a JSON file
               
        Exemple:
        >>> eq = Equipe()
        >>> eq.save()
        """
        listPoke = []
        for el in range(len(self.equipePokemon)):
            poke = {
	        "nom": self.getPokemon(el).getChocobos().getName(),
	        "type": self.getPokemon(el).getChocobos().getType(),
	        "PNG": self.getPokemon(el).getChocobos().getPng(),
	        "PNGdos": self.getPokemon(el).getChocobos().getPngBack()
            }
            listPoke.append(poke)


        with open('src/Game/equipe/equipe.json','w') as file:
            json.dump(listPoke,file, indent = 2)
