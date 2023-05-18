import unittest

from equipe.equipe import *
from equipe.pokeball import *
from IA import *
from Toir.Shocobos.Capacite.abstract_capacite import *
from Toir.Shocobos.Capacite.aquaFlow import *
from Toir.Shocobos.Capacite.chauffe import *
from Toir.Shocobos.Capacite.electaser import *
from Toir.Shocobos.Capacite.lancepierre import *
from Toir.Shocobos.Capacite.plantattack import *
from Toir.Shocobos.Capacite.tackle import *
from Toir.Shocobos.Chocobos import *
from Toir.Shocobos.Status.Effet import *
from Toir.Shocobos.Status.Status import *
from Toir.Shocobos.Status.Status_Nul import *
from Toir.Shocobos.Type import *


class testEquipe(unittest.TestCase):

    def testGetpokemonExist(self):
        eq = Equipe()
        self.assertEqual(isinstance(eq.getPokemon(2),Chocobos),True)
    
    def testGetpokemonNotExist(self):
        eq = Equipe()
        self.assertEqual(eq.getPokemon(5),False)

    def testTaille(self):
        eq = Equipe()
        self.assertEqual(eq.taille(),2)

    def testchangementPokemon(self):
        eq = Equipe()
        Choco3 = eq.getPokemon(2)
        eq.changementPokemon(2)
        poke = eq.getPokemon(2)
        self.assertEqual(poke,Choco3)
    
    def testAjoutPokemon(self):
        randomChoco = Chocobos()
        eq = Equipe()
        eq.ajoutPokemon(randomChoco)
        self.assertEqual(eq.getPokemon(3).getChocobos().getName(), randomChoco.getChocobos().getName())

    def testSave(self):
        eq = Equipe()
        eq.save()



class testPokeball(unittest.TestCase):

    def testPokeball(self):
        eq = Equipe()
        randomChocobo = Chocobos()
        for i in range(1,100):
            Pokeball(eq,randomChocobo)
        self.assertEqual(eq.getPokemon(3).getChocobos().getName(),randomChocobo.getChocobos().getName())

class testAbstractAbility(unittest.TestCase):

    def testgetName(self):
        ability = AbstractAbility()
        self.assertEqual(ability.getName(),False)

    def testgetType(self):
        ability = AbstractAbility()
        self.assertEqual(ability.getType(),False)

    def testgetCategory(self):
        ability = AbstractAbility()
        self.assertEqual(ability.getCategory(),False)

    def testgetAccuracy(self):
        ability = AbstractAbility()
        self.assertEqual(ability.getAccuracy(),False)

    def testgetPower(self):
        ability = AbstractAbility()
        self.assertEqual(ability.getPower(),False)
    
    def testsetReceiver(self):
        ability = AbstractAbility()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        self.assertEqual(ability.receiver,chocobEnemis)

    def testsetLauncher(self):
        ability = AbstractAbility()
        chocobAllier = Chocobos()
        ability.setLauncher(chocobAllier)
        self.assertEqual(ability.launcher,chocobAllier)

    def testgetStatus(self):
        ability = AbstractAbility()
        self.assertEqual(isinstance(ability.getStatus(),Status_Nul),True)

    def testgetBoost(self):
        ability = AbstractAbility()
        self.assertEqual(ability.getBoost().getMatrice(),[(0,0,0,0),(0,0,0,0)])

    def testgetDes(self):
        ability = AbstractAbility()
        self.assertEqual(ability.getDes().getMatrice(),[(0,0,0,0),(0,0,0,0)])
    
    def testapplique(self):
        ability = AbstractAbility()
        chocobAllier = Chocobos()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        ability.setLauncher(chocobAllier)
        ability.applique()
        self.assertEqual(ability.getDegats(),0)
    
class testaquaFlowAbility(unittest.TestCase):

    def testgetName(self):
        ability = aquaFlowAbility()
        self.assertEqual(ability.getName(),'Aqua Flow')

    def testgetType(self):
        ability = aquaFlowAbility()
        self.assertEqual(ability.getType().getNomType(),'eau')

    def testgetCategory(self):
        ability = aquaFlowAbility()
        self.assertEqual(ability.getCategory(),"SPECIAL")

    def testgetAccuracy(self):
        ability = aquaFlowAbility()
        self.assertEqual(ability.getAccuracy(),100)

    def testgetPower(self):
        ability = aquaFlowAbility()
        self.assertEqual(ability.getPower(),60)
    
    def testsetReceiver(self):
        ability = aquaFlowAbility()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        self.assertEqual(ability.receiver,chocobEnemis)

    def testsetLauncher(self):
        ability = aquaFlowAbility()
        chocobAllier = Chocobos()
        ability.setLauncher(chocobAllier)
        self.assertEqual(ability.launcher,chocobAllier)

    def testgetStatus(self):
        ability = aquaFlowAbility()
        self.assertEqual(isinstance(ability.getStatus(),Status_Nul),True)

    def testgetBoost(self):
        ability = aquaFlowAbility()
        self.assertEqual(ability.getBoost().getMatrice(),[(0,0,0,0),(0,0,0,0)])

    def testgetDes(self):
        ability = aquaFlowAbility()
        self.assertEqual(ability.getDes().getMatrice(),[(0,0,0,0),(0,0,0,0)])
    
    def testapplique(self):
        ability = aquaFlowAbility()
        chocobAllier = Chocobos()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        ability.setLauncher(chocobAllier)
        ability.applique()
        self.assertEqual(ability.getDegats()!=0 , True)

class testChauffeAbility(unittest.TestCase):

    def testgetName(self):
        ability = ChauffeAbility()
        self.assertEqual(ability.getName(),'chauffe')

    def testgetType(self):
        ability = ChauffeAbility()
        self.assertEqual(ability.getType().getNomType(),"feu")

    def testgetCategory(self):
        ability = ChauffeAbility()
        self.assertEqual(ability.getCategory(),"SPECIAL")

    def testgetAccuracy(self):
        ability = ChauffeAbility()
        self.assertEqual(ability.getAccuracy(),100)

    def testgetPower(self):
        ability = ChauffeAbility()
        self.assertEqual(ability.getPower(),60)
    
    def testsetReceiver(self):
        ability = ChauffeAbility()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        self.assertEqual(ability.receiver,chocobEnemis)

    def testsetLauncher(self):
        ability = ChauffeAbility()
        chocobAllier = Chocobos()
        ability.setLauncher(chocobAllier)
        self.assertEqual(ability.launcher,chocobAllier)

    def testgetStatus(self):
        ability = ChauffeAbility()
        self.assertEqual(isinstance(ability.getStatus(),Status_Nul),True)

    def testgetBoost(self):
        ability = ChauffeAbility()
        self.assertEqual(ability.getBoost().getMatrice(),[(0,0,0,0),(0,0,0,0)])

    def testgetDes(self):
        ability = ChauffeAbility()
        self.assertEqual(ability.getDes().getMatrice(),[(0,0,0,0),(0,0,0,0)])
    
    def testapplique(self):
        ability = ChauffeAbility()
        chocobAllier = Chocobos()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        ability.setLauncher(chocobAllier)
        ability.applique()
        self.assertEqual(ability.getDegats()!=0 , True)

class testelectaserAbility(unittest.TestCase):

    def testgetName(self):
        ability = electaserAbility()
        self.assertEqual(ability.getName(),'Electaser')

    def testgetType(self):
        ability = electaserAbility()
        self.assertEqual(ability.getType().getNomType(),"electrique")

    def testgetCategory(self):
        ability = electaserAbility()
        self.assertEqual(ability.getCategory(),"SPECIAL")

    def testgetAccuracy(self):
        ability = electaserAbility()
        self.assertEqual(ability.getAccuracy(),100)

    def testgetPower(self):
        ability = electaserAbility()
        self.assertEqual(ability.getPower(),60)
    
    def testsetReceiver(self):
        ability = electaserAbility()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        self.assertEqual(ability.receiver,chocobEnemis)

    def testsetLauncher(self):
        ability = electaserAbility()
        chocobAllier = Chocobos()
        ability.setLauncher(chocobAllier)
        self.assertEqual(ability.launcher,chocobAllier)

    def testgetStatus(self):
        ability = electaserAbility()
        self.assertEqual(isinstance(ability.getStatus(),Status_Nul),True)

    def testgetBoost(self):
        ability = electaserAbility()
        self.assertEqual(ability.getBoost().getMatrice(),[(0,0,0,0),(0,0,0,0)])

    def testgetDes(self):
        ability = electaserAbility()
        self.assertEqual(ability.getDes().getMatrice(),[(0,0,0,0),(0,0,0,0)])
    
    def testapplique(self):
        ability = electaserAbility()
        chocobAllier = Chocobos()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        ability.setLauncher(chocobAllier)
        ability.applique()
        self.assertEqual(ability.getDegats()!=0 , True)

class testLancepierreAbility(unittest.TestCase):

    def testgetName(self):
        ability = LancepierreAbility()
        self.assertEqual(ability.getName(),'Lance Pierre')

    def testgetType(self):
        ability = LancepierreAbility()
        self.assertEqual(ability.getType().getNomType(),"sol")

    def testgetCategory(self):
        ability = LancepierreAbility()
        self.assertEqual(ability.getCategory(),"PHYSICAL")

    def testgetAccuracy(self):
        ability = LancepierreAbility()
        self.assertEqual(ability.getAccuracy(),100)

    def testgetPower(self):
        ability = LancepierreAbility()
        self.assertEqual(ability.getPower(),20)
    
    def testsetReceiver(self):
        ability = LancepierreAbility()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        self.assertEqual(ability.receiver,chocobEnemis)

    def testsetLauncher(self):
        ability = LancepierreAbility()
        chocobAllier = Chocobos()
        ability.setLauncher(chocobAllier)
        self.assertEqual(ability.launcher,chocobAllier)

    def testgetStatus(self):
        ability = LancepierreAbility()
        self.assertEqual(isinstance(ability.getStatus(),Status_Nul),True)

    def testgetBoost(self):
        ability = LancepierreAbility()
        self.assertEqual(ability.getBoost().getMatrice(),[(0,0,0,0),(0,0,0,0)])

    def testgetDes(self):
        ability = LancepierreAbility()
        self.assertEqual(ability.getDes().getMatrice(),[(0,0,0,0),(0,0,0,0)])
    
    def testapplique(self):
        ability = LancepierreAbility()
        chocobAllier = Chocobos()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        ability.setLauncher(chocobAllier)
        ability.applique()
        self.assertEqual(ability.getDegats()!=0 , True)

class testPlantattackAbility(unittest.TestCase):

    def testgetName(self):
        ability = PlantattackAbility()
        self.assertEqual(ability.getName(),'Plantattack')

    def testgetType(self):
        ability = PlantattackAbility()
        self.assertEqual(ability.getType().getNomType(),"plante")

    def testgetCategory(self):
        ability = PlantattackAbility()
        self.assertEqual(ability.getCategory(),"PHYSICAL")

    def testgetAccuracy(self):
        ability = PlantattackAbility()
        self.assertEqual(ability.getAccuracy(),100)

    def testgetPower(self):
        ability = PlantattackAbility()
        self.assertEqual(ability.getPower(),20)
    
    def testsetReceiver(self):
        ability = PlantattackAbility()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        self.assertEqual(ability.receiver,chocobEnemis)

    def testsetLauncher(self):
        ability = PlantattackAbility()
        chocobAllier = Chocobos()
        ability.setLauncher(chocobAllier)
        self.assertEqual(ability.launcher,chocobAllier)

    def testgetStatus(self):
        ability = PlantattackAbility()
        self.assertEqual(isinstance(ability.getStatus(),Status_Nul),True)

    def testgetBoost(self):
        ability = PlantattackAbility()
        self.assertEqual(ability.getBoost().getMatrice(),[(0,0,0,0),(0,0,0,0)])

    def testgetDes(self):
        ability = PlantattackAbility()
        self.assertEqual(ability.getDes().getMatrice(),[(0,0,0,0),(0,0,0,0)])
    
    def testapplique(self):
        ability = PlantattackAbility()
        chocobAllier = Chocobos()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        ability.setLauncher(chocobAllier)
        ability.applique()
        self.assertEqual(ability.getDegats()!=0 , True)

class testTackleAbility(unittest.TestCase):

    def testgetName(self):
        ability = TackleAbility()
        self.assertEqual(ability.getName(),'tackle')

    def testgetType(self):
        ability = TackleAbility()
        self.assertEqual(ability.getType().getNomType(),"vol")

    def testgetCategory(self):
        ability = TackleAbility()
        self.assertEqual(ability.getCategory(),"PHYSICAL")

    def testgetAccuracy(self):
        ability = TackleAbility()
        self.assertEqual(ability.getAccuracy(),100)

    def testgetPower(self):
        ability = TackleAbility()
        self.assertEqual(ability.getPower(),20)
    
    def testsetReceiver(self):
        ability = TackleAbility()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        self.assertEqual(ability.receiver,chocobEnemis)

    def testsetLauncher(self):
        ability = TackleAbility()
        chocobAllier = Chocobos()
        ability.setLauncher(chocobAllier)
        self.assertEqual(ability.launcher,chocobAllier)

    def testgetStatus(self):
        ability = TackleAbility()
        self.assertEqual(isinstance(ability.getStatus(),Status_Nul),True)

    def testgetBoost(self):
        ability = TackleAbility()
        self.assertEqual(ability.getBoost().getMatrice(),[(0,0,0,0),(0,0,0,0)])

    def testgetDes(self):
        ability = TackleAbility()
        self.assertEqual(ability.getDes().getMatrice(),[(0,0,0,0),(0,0,0,0)])
    
    def testapplique(self):
        ability = TackleAbility()
        chocobAllier = Chocobos()
        chocobEnemis = Chocobos()
        ability.setReceiver(chocobEnemis)
        ability.setLauncher(chocobAllier)
        ability.applique()
        self.assertEqual(ability.getDegats()!=0 , True)

class testEffet(unittest.TestCase):

    def testchangement(self):
        test = Effet(matrice = [(1,0,1,0), (0,1,0,1)])
        test.changement([(1,0,1,0), (0,0,0,0)])
        self.assertEqual(test.getAtk(),1)
        self.assertEqual(test.getDef(),0)
        self.assertEqual(test.getAtkSpe(),1)
        self.assertEqual(test.getDefSpe(),0)
    
    def testgetAtk(self):
        test = Effet()
        self.assertEqual(test.getAtk(),0)

    def testgetDef(self):
        test = Effet()
        self.assertEqual(test.getDef(),0)

    def testgetAtkSpe(self):
        test = Effet()
        self.assertEqual(test.getAtkSpe(),0)

    def testgetDefSpe(self):
        test = Effet()
        self.assertEqual(test.getDefSpe(),0)

    def testgetMatrice(self):
        test = Effet(matrice = [(1,0,1,0), (0,1,0,1)])
        self.assertEqual(test.getMatrice(),[(1,0,1,0), (0,1,0,1)])


class testStatus(unittest.TestCase):

    def testgetPourcDegat(self):
        sta = Status()
        self.assertEqual(sta.getPourcDegat(),0)

    def testgetNbTourLeft(self):
        sta = Status()
        self.assertEqual(sta.getNbTourLeft(),0)

    def testgetPassTurn(self):
        sta = Status()
        self.assertEqual(sta.getPassTurn(),False)

    def testnextTurn(self):
        sta = Status()
        self.assertEqual(sta.nextTurn(),False)

class testStatus_Nul(unittest.TestCase):

    def testgetPourcDegat(self):
        sta = Status_Nul()
        self.assertEqual(sta.getPourcDegat(),0)

    def testgetNbTourLeft(self):
        sta = Status_Nul()
        self.assertEqual(sta.getNbTourLeft(),-1)

    def testgetPassTurn(self):
        sta = Status_Nul()
        self.assertEqual(sta.getPassTurn(),False)

    def testnextTurn(self):
        sta = Status_Nul()
        self.assertEqual(sta.nextTurn(),False)

class testStatus_Lethargie(unittest.TestCase):

    def testgetPourcDegat(self):
        sta = Status_Lethargie()
        self.assertEqual(sta.getPourcDegat(),0)

    def testgetNbTourLeft(self):
        sta = Status_Lethargie()
        self.assertEqual(sta.getNbTourLeft(),3)

    def testgetPassTurn(self):
        sta = Status_Lethargie()
        self.assertEqual(sta.getPassTurn(),True)

    def testnextTurn(self):
        sta = Status_Lethargie()
        sta.nextTurn()
        self.assertEqual(sta.getNbTourLeft(),2)

class testStatus_Flambee(unittest.TestCase):

    def testgetPourcDegat(self):
        sta = Status_Flambee()
        self.assertEqual(sta.getPourcDegat(),8)

    def testgetNbTourLeft(self):
        sta = Status_Flambee()
        self.assertEqual(sta.getNbTourLeft(),4)

    def testgetPassTurn(self):
        sta = Status_Flambee()
        self.assertEqual(sta.getPassTurn(),False)

    def testnextTurn(self):
        sta = Status_Flambee()
        sta.nextTurn()
        self.assertEqual(sta.getNbTourLeft(),3)
    
class testStatus_Deboussoler(unittest.TestCase):

    def testgetPourcDegat(self):
        sta = Status_Deboussoler()
        self.assertEqual(sta.getPourcDegat(),20)

    def testgetNbTourLeft(self):
        sta = Status_Deboussoler()
        self.assertEqual(sta.getNbTourLeft(),1)

    def testgetPassTurn(self):
        sta = Status_Deboussoler()
        self.assertEqual(sta.getPassTurn(),True)

    def testnextTurn(self):
        sta = Status_Deboussoler()
        self.assertEqual(sta.nextTurn(),False)

class TestType(unittest.TestCase):

    def testAvantage(self):
        ty = Type('feu')
        self.assertEqual(ty.avantage(),[EnumType.plante])
    
    def testDesavantage(self):
        ty = Type('feu')
        self.assertEqual(ty.desavantage(),[EnumType.feu, EnumType.eau])




if __name__ == '__main__':
    unittest.main()