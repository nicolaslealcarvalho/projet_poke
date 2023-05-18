from Toir.Shocobos.Status.Effet import *
from Toir.Shocobos.Status.Status import *
from Toir.Shocobos.Status.Status_Nul import *
from random import *
from Toir.Shocobos.EnumType import *
import json
from Toir.Shocobos.Capacite.aquaFlow import *
from Toir.Shocobos.Capacite.chauffe import *
from Toir.Shocobos.Capacite.electaser import *
from Toir.Shocobos.Capacite.lancepierre import *
from Toir.Shocobos.Capacite.plantattack import *
from Toir.Shocobos.Capacite.tackle import *

class GenerateChocobos():
    """
    this classe allow to generate chocobos with their stat, name associate with his png and capacity that he will be able to use
    """

    def __init__(self) :
        self._Pv = randint(80,120) 
        #self.__PNG
        #self.__Type = random.randint(80,120)
        with open('src/Game/Toir/Shocobos/ChocoboL.json') as mon_fichier:
            data = json.load(mon_fichier)
        self._NometTypePng= choice(data)
        self._Att = randint(25,75) # a voir si l'ecart n'est pas trop grand
        self._Def = randint(30,80) 
        self._AttSpe = randint(20,70) 
        self._DefSpe = randint(10,60)
        self.listeCapaciter = []
        self.allCapaciter = [aquaFlowAbility(),ChauffeAbility(),electaserAbility(),LancepierreAbility(),PlantattackAbility(),TackleAbility()]
        while len(self.listeCapaciter)!= 4 :
            a = choice(self.allCapaciter)
            if a not in self.listeCapaciter:
                self.listeCapaciter.append(a)


    def getName(self):
        """
        this method return the name of the chocobos

        Return: the name of the chocobos
        """
        return self._NometTypePng["nom"]
    

    def getType(self):
        """
        this method return the type of the chocobos

        Return: the type of the chocobos
        """
        return self._NometTypePng["type"]
    

    def getPng(self):
        """
        this method return the Png of the chocobos

        Return: the Png of the chocobos
        """
        return self._NometTypePng["PNG"]
    

    def getPngBack(self):
        """
        this method return the back Png of the chocobos

        Return: the back Png of the chocobos
        """
        return self._NometTypePng["PNGdos"]


    def getCapacity(self):
        """
        this method return the list of the capacity that the Chocobo can use

        Return: the list of all attack of the Chocobo        
        """
        return self.listeCapaciter


    def getPv(self) :
        """
        this method return the Pv of the chocobos

        Return: the Pv of the chocobos
        """
        return self._Pv
    

    def getAtt(self) :
        """
        this method return the Attack of the chocobos

        Return: the Attack of the chocobos
        """
        return self._Att


    def getDef(self) :
        """
        this method return the Defence of the chocobos

        Return: the Defence of the chocobos
        """
        return self._Def
    

    def getAttSpe(self) :
        """
        this method return the Special Attack of the chocobos

        Return: the Special Attack of the chocobos
        """
        return self._AttSpe
    

    def getDefSpe(self) :
        """
        this method return the Special Defence of the chocobos

        Return: the Special Defence of the chocobos
        """
        return self._DefSpe

    def createChocobosHeroes(self):
        """
        this method create a Chocobos call Chocobos Heros with static statistic         
        """
        self._Pv = 120
        self._Att = 25
        self._AttSpe = 10
        self._Def = 15
        self._DefSpe = 5
        with open('src/Game/Toir/Shocobos/ChocoboL.json') as mon_fichier:
            data = json.load(mon_fichier)
        self._NometTypePng =  data[0]

    def generateFromJson (self,dict):
        self._NometTypePng =  dict

    





class Chocobos() : 
    """
    this class is use to manage a Chocobos 
    """
    def __init__(self) :
        self.generatedChocobo = GenerateChocobos()
        self.Status = Status_Nul()
        self.Effet = Effet()
        self._PvActuel = self.generatedChocobo.getPv()

    def generatedChocoboHero(self):
        """
        this method allow to create the Chocobo hero
        """
        self.generatedChocobo.createChocobosHeroes()
        self._PvActuel = self.generatedChocobo.getPv()

    def getChocobos(self):
        """
        this method allow to get the generated chocobo traited by this class

        Return: the chocobos
        """
        return self.generatedChocobo

    def changePV(self, degat):
        """
        this method  allow to manipulate the hp of the chocobo, if the hp are equals to 0 this method will send a end fight message
        """
        self._PvActuel = self._PvActuel - degat
        if self._PvActuel <= 0 :
            self.endFight()

    def getPvActuel(self):
        """
        this method allow the users to get the actual hp of the Chocobo

        Return: the actual Hp of the Chocobo
        """
        return self._PvActuel

    def changeStatus(self,StatusApliquer):
        """
        this method allow to change the status of the Chocobo
        """
        if self.Status == Status_Nul():
            self.Status = StatusApliquer

    def changeEffet(self,listChang):
        """
        this method allow to change the Effect of the Chocobo
        """
        self.Effet.changement(listChang)

    def nextTurn(self):
        """
        this method allow to pass a turn to aplicate status effect to the Chocobo
        """
        if self.Status != Status_Nul():
            self._PvActuel -= self.Status.getPourcDegat * self._PvActuel
            self.Status.nextTurn

    def  noHpLeft(self):
        """
        this method allow the user to know if the chocobo has no more hp

        Return: True if the chocobo has not hp anymore, False otherwise
        """
        return self._PvActuel <= 0

    def endFight(self):
        """
        this method is use to close the interface(obselete)
        """
        #quitter l'interface
        pass

    def choixCap(self):
        """
        this method is use to choose what capacity the chocobo will use(obselete)
        """
        #pas encore les capaciter a choisir
        pass



