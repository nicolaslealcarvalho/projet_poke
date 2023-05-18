from Toir.Shocobos.Status.Status_Nul import *
from Toir.Shocobos.Status.Status_Deboussoler import *
from Toir.Shocobos.Status.Status_Flambee import *
from Toir.Shocobos.Status.Status_Lethargie import *

class IA:
    """
    The class IA define the attack the adversarie chocobos will choose,

    Args:
        pokemonAllier (Chocobos): the chocobos that will use the capacity
        pokemonEnemis (Chocobos): the chocobos that will receive the attack

    Attributes:
        capacity (list(Capaciter)): the list of every capacity that the pokemonAllier has

    Example:
        ChocobosE = Chocobos()
        ChocobosA = Chocobos()
        >>> ia = IA(ChocobosA,ChocobosE)
    
    """

    def __init__(self,pokemonAllier,pokemonEnemis):
        self.pokemonAllier = pokemonAllier
        self.capacity = self.pokemonAllier.getChocobos().getCapacity()
        self.pokemonEnnemis = pokemonEnemis
        for i in self.capacity:
            i.setReceiver(pokemonEnemis)
            i.setLauncher(pokemonAllier)

    def choiseCap(self):
        os = self.CanOS()
        statut = self.statusOnHit()
        #boost = self.Boost()
        #effect = self.EffectOnHit()
        dam = self.JustDamage()
        liste = statut #+ boost + effect
        if os != []:
            os[0].applique()
        elif liste != [] :
            choose = self.most_frequent(liste)
            choose.applique()
        else :
            dam.applique()

    
    def CanOS(self):
        listAccept= []
        for i in self.capacity:
            deg = i.getPower()* self.pokemonAllier.getChocobos().getAtt() // self.pokemonEnnemis.getChocobos().getDef() - self.pokemonAllier.getPvActuel()
            if (deg>=0):
                listAccept.append(i)
        return listAccept
                        
    def statusOnHit(self):
        listAccept = []
        for i in self.capacity:
            if(i.getStatus() is not Status_Nul):
                listAccept.append(i)
        return listAccept

    def Boost(self):
        listAccept = []
        for i in self.capacity:
            if(i.getBoost()[0] != (0,0,0,0)):
                listAccept.append(i)
        return listAccept

    def EffectOnHit(self):
        listAccept = []
        for i in self.capacity:
            if(i.getDes()[1] != (0,0,0,0)):
                listAccept.append(i)
        return listAccept

    def JustDamage(self):
        cap = self.capacity[0]
        for i in self.capacity:
            if i.getPower() > cap.getPower():
                cap = i
        return cap
    
    def most_frequent(self,List):
        counter = 0
        num = List[0]
        
        for i in List:
            curr_frequency = List.count(i)
            if(curr_frequency> counter):
                counter = curr_frequency
                num = i
    
        return num
    


