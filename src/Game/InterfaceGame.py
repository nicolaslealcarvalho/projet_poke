import pygame
from Toir.Shocobos.Chocobos import *
from Toir.battle.background import *
import sound
from equipe.equipe import *
from equipe.pokeball import *
from IA import *

#config.path = ""

class interfaceGame:

    def __init__(self, sound: 'sound.Sound' = sound.BATTLE):
        
        pygame.init()
        pygame.font.init()

        #self.ChocobosAllier = Chocobos()
        #self.ChocobosAllier.generatedChocoboHero() #si none type probleme de retrun

        self.equ = Equipe()
        self.ChocobosAllier = self.equ.getPokemon(0)
        self.ChocobosEnnemis = Chocobos()
        self.atackOn = False
        self.equOn = False
        self.objOn = False

        self.sound: 'sound.Sound' = sound
        #pygame.mixer.Sound('assets/sound/music/Pokemon-Go.wav')

        self.RUNNING = True
        
        self.fenetre = pygame.display.set_mode((800,600))
        
        self.myfont = pygame.font.SysFont('Helvetic', 20)
        
        self.bg = pygame.image.load("assets/textures/battle/bg/forest.png") #(config.path+"assets/textures/battle/bg/forest.png")
        #self.bg = FOREST
        # taille : 800 480 p
        

        self.grass = pygame.image.load("assets/textures/battle/base.png")
        self.grass.subsurface(pygame.Rect(650, 480, 150, 60))

        self.hudEnemie = pygame.image.load("assets/textures/hud/HUD.png")
        # taille : 400 400 p

        self.baseEnemie = pygame.image.load("assets/textures/battle/base_ennemi.png")

        self.basePlayer = pygame.image.load("assets/textures/battle/base_player.png")

        self.hudPlayer = pygame.image.load("assets/textures/hud/HUD.png")
        # taille : 400 400 p

        self.start_sound: pygame.mixer.Sound = pygame.mixer.Sound('assets/sound/music/Pokemon-Go.wav')
        pygame.mixer.Sound.play(self.start_sound)

        self.pokeAllier = pygame.image.load(self.ChocobosAllier.getChocobos().getPngBack())
        self.pokeAllier = pygame.transform.scale(self.pokeAllier, (300, 300))

        self.pokeEne = pygame.image.load(self.ChocobosEnnemis.getChocobos().getPng())
        self.pokeEne = pygame.transform.scale(self.pokeEne, (300, 300))

        self.curentHpAlier = self.myfont.render(str(self.ChocobosAllier.getChocobos().getPv()), False, (0,0,0))
        self.curentHpEnem = self.myfont.render(str(self.ChocobosEnnemis.getChocobos().getPv()), False, (0,0,0))

        self.MaxHpAllier = self.myfont.render(str(self.ChocobosAllier.getChocobos().getPv()), False, (0,0,0))
        self.MaxHpEnem = self.myfont.render(str(self.ChocobosEnnemis.getChocobos().getPv()), False, (0,0,0))

        self.nomPokeAllier = self.myfont.render(self.ChocobosAllier.getChocobos().getName(), False, (0,0,0))
        self.nomPokeEnemis = self.myfont.render(self.ChocobosEnnemis.getChocobos().getName(), False, (0,0,0))



        self.barreVieEvolutiveAllier = (517, 427, 130, 5)
        self.barreVieEvolutiveEnemie = (50, 48, 130, 5)
        pygame.draw.rect(self.fenetre,(0,100,0),pygame.Rect(self.barreVieEvolutiveAllier))
        pygame.draw.rect(self.fenetre,(0,100,0),pygame.Rect(self.barreVieEvolutiveEnemie))

    def gerer_events_principale(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.time.wait(200)
            if event.type == pygame.QUIT:
                self.RUNNING = False
 
    def load_assets(self):
        self.sound.load()
        sound.BATTLE.load()

    # gestion des hp

    def affichageHpAllier (self):
        #pygame.time.delay(1500)
        self.curentHpAlier = self.myfont.render(str(self.ChocobosAllier.getPvActuel()), False, (0,0,0))

    def affichageHpEne (self):
        #pygame.time.delay(1500)
        self.curentHpEnem = self.myfont.render(str(self.ChocobosEnnemis.getPvActuel()), False, (0,0,0))


    # gestion du texte en combat


    def affichageTexte(self):
        pygame.draw.rect(
            self.fenetre,
            (255,255,255),
            pygame.Rect(0, 480, 500, 120))
        pygame.draw.rect(
            self.fenetre,
            (0,0,0),
            pygame.Rect(0, 480, 500, 120),1)
        
        
    def prompt(self,txt):
        self.affichageTexte()
        text = self.myfont.render(txt, False, (0,0,0))
        self.fenetre.blit(text, (20, 490))
        self.Maj()
        self.gererBarVieAllier()
        self.gererBarVieEnemis()
        
        self.fenetre.blit(self.curentHpAlier, (520,435))
        self.fenetre.blit(self.curentHpEnem, (50,55))
        self.fenetre.blit(self.MaxHpAllier, (545,435))
        self.fenetre.blit(self.MaxHpEnem, (75,55))

        self.fenetre.blit(self.nomPokeAllier, (518, 413))
        self.fenetre.blit(self.nomPokeEnemis, (50, 35))
        pygame.display.update()
        pygame.time.delay(2000)
        
        


    # gestion des menus

    def créerMenu(self, positions,type):
        rect = pygame.draw.rect(
            self.fenetre,
            (0,0,0),
            pygame.Rect(positions[0], positions[1], positions[2], positions[3]),1)
        text = self.myfont.render(type, False, (0,0,0))
        self.fenetre.blit(text, (positions[0], positions[1]))
        self.gererMenu(rect,type)


    def gererMenu(self, rectangle,type):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]: # UP
            mouse_pos = pygame.mouse.get_pos()
                    
            if rectangle.collidepoint(mouse_pos):
                match type :
                    case 'Attaque':
                        print('Cliqué sur attaque')
                        self.atackOn = True
                    case 'Pokemon':
                        print('Cliqué sur Pokmeon')
                        self.equOn = True
                    case 'Objet':
                        print('Cliqué sur objet')
                        self.objOn = True
                    case 'Fuite':
                        print('Cliqué sur Fuite')
                        self.equ.save()
                        self.RUNNING = False
    
    
    # gerer les menu d'attaque

    def menuAttaque(self,positions, index):
        rect = pygame.draw.rect(
            self.fenetre,
            (0,0,0),
            pygame.Rect(positions[0], positions[1], positions[2], positions[3]),1)
    
        text = self.myfont.render(self.ChocobosAllier.getChocobos().getCapacity()[index].getName(), False, (0,0,0))
        self.fenetre.blit(text, (positions[0], positions[1]))

        self.gererMenuAttaque(rect,index)
    

    def menuAffichageAttaque(self):
            pygame.draw.rect(
            self.fenetre,
            (255,255,255),
            pygame.Rect(0, 480, 500, 120))
            pygame.draw.rect(
            self.fenetre,
            (0,0,0),
            pygame.Rect(0, 480, 500, 120),1)   

    def gererMenuAttaque(self,rectangle,index):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]: # UP
            mouse_pos = pygame.mouse.get_pos()
            
            if rectangle.collidepoint(mouse_pos):
                print("Cliqué sur attaque {0}".format(index+1))
                self.atackOn = False
                atk = self.ChocobosAllier.getChocobos().getCapacity()[index]
                atk.setLauncher(self.ChocobosAllier)
                atk.setReceiver(self.ChocobosEnnemis)
                atk.applique()
                self.prompt(self.ChocobosAllier.getChocobos().getName() + " utilise "+ atk.getName())
                pygame.display.update()

                self.prompt(self.ChocobosEnnemis.getChocobos().getName() + " attaque")
                pygame.display.update()
                self.attAdversaire()   

    def attAdversaire(self):
        a = IA(self.ChocobosEnnemis,self.ChocobosAllier)
        a.choiseCap()

     #gestion des menu de changement de pokemon
    def menuPoke(self, positions, index):
        rect = pygame.draw.rect(
            self.fenetre,
            (0,0,0),
            pygame.Rect(positions[0], positions[1], positions[2], positions[3]),1)
    
        text = self.myfont.render(self.equ.getPokemon(index).getChocobos().getName(), False, (0,0,0))
        self.fenetre.blit(text, (positions[0], positions[1]))

        self.gererMenuPoke(rect,index)
        

    def menuAffichagePoke(self):
            pygame.draw.rect(
            self.fenetre,
            (255,255,255),
            pygame.Rect(0, 480, 350, 120))
            pygame.draw.rect(
            self.fenetre,
            (0,0,0),
            pygame.Rect(0, 480, 350, 120),1)

    def gererMenuPoke(self,rectangle,index):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]: # UP
            mouse_pos = pygame.mouse.get_pos()
            
            if rectangle.collidepoint(mouse_pos):     
                self.equ.changementPokemon(index+1)
                self.ChocobosAllier = self.equ.getPokemon(0)
                #self.attAdversaire()
                self.prompt(self.ChocobosAllier.getChocobos().getName() + " changement ")
                self.equOn = False
                if index != 0 :
                    self.prompt(self.ChocobosEnnemis.getChocobos().getName() + " attaque")
                    pygame.display.update()
                    self.attAdversaire()


    def menuObjet1(self):
        
        rect = pygame.draw.rect(
            self.fenetre,
            (0,0,0),
            pygame.Rect(500, 480, 150, 60),1)
        text = self.myfont.render(" pokeball ", False, (0,0,0))
        self.fenetre.blit(text, (500, 480))
        self.gererMenuObjet1(rect)

    def gererMenuObjet1(self,rectangle):
        
        mouse = pygame.mouse.get_pressed()
        if mouse[0]: # UP
            mouse_pos = pygame.mouse.get_pos()
            
            if rectangle.collidepoint(mouse_pos): 
                
                tailleEquipeAv = self.equ.taille()
                Pokeball(self.equ,self.ChocobosEnnemis)
                tailleEquipeAp = self.equ.taille()
                if tailleEquipeAv < tailleEquipeAp:
                    self.prompt("vous avez capturer le pokemon")
                    self.RUNNING = False
                    pygame.display.update()
                    self.equ.save()
                else:
                    self.prompt("le " + self.ChocobosEnnemis.getChocobos().getName() + " c'est échappé de la pokeball")
                    pygame.display.update()
                    self.prompt(self.ChocobosEnnemis.getChocobos().getName() + " attaque")
                    pygame.display.update()
                    self.attAdversaire()
                self.objOn = False
                

    #gestion des bars de vie

    def gererBarVieAllier(self):
        x = (self.ChocobosAllier.getPvActuel() / self.ChocobosAllier.getChocobos().getPv()) * 130
        self.barreVieEvolutiveAllier = (517, 427, x, 5)
        if x > 65:
            pygame.draw.rect(self.fenetre,(0,100,0),pygame.Rect(self.barreVieEvolutiveAllier))
        elif x > 26:
            pygame.draw.rect(self.fenetre,(255,255,0),pygame.Rect(self.barreVieEvolutiveAllier))
        else:
            pygame.draw.rect(self.fenetre,(255,0,0),pygame.Rect(self.barreVieEvolutiveAllier))
        if self.ChocobosAllier.noHpLeft():
            self.ChocoMort()
        self.curentHpAlier = self.myfont.render(str(self.ChocobosAllier.getPvActuel()), False, (0,0,0))

    def gererBarVieEnemis(self):
        x = (self.ChocobosEnnemis.getPvActuel() / self.ChocobosEnnemis.getChocobos().getPv()) * 130
        self.barreVieEvolutiveEnemie = (50, 48, x , 5)
        if x > 65:
            pygame.draw.rect(self.fenetre,(0,100,0),pygame.Rect(self.barreVieEvolutiveEnemie))
        elif x > 26:
            pygame.draw.rect(self.fenetre,(255,255,0),pygame.Rect(self.barreVieEvolutiveEnemie))
        else:
            pygame.draw.rect(self.fenetre,(255,0,0),pygame.Rect(self.barreVieEvolutiveEnemie))
        if self.ChocobosEnnemis.noHpLeft():
            self.RUNNING = False
        self.curentHpEnem = self.myfont.render(str(self.ChocobosEnnemis.getPvActuel()), False, (0,0,0))


    def ChocoMort(self):
        if self.ChocobosAllier.noHpLeft():
            if not self.equ.getPokemon(1).noHpLeft():
                self.equOn = True
            elif not self.equ.getPokemon(2).noHpLeft():
                self.equOn = True
            elif not self.equ.getPokemon(3).noHpLeft():
                self.equOn = True
            elif not self.equ.getPokemon(4).noHpLeft():
                self.equOn = True
            elif not self.equ.getPokemon(5).noHpLeft():
                self.equOn = True
            else :
                self.RUNNING = False

    # mise a jour

    def Maj(self):
        self.pokeAllier = pygame.image.load(self.ChocobosAllier.getChocobos().getPngBack())
        self.pokeAllier = pygame.transform.scale(self.pokeAllier, (300, 300))

        self.pokeEne = pygame.image.load(self.ChocobosEnnemis.getChocobos().getPng())
        self.pokeEne = pygame.transform.scale(self.pokeEne, (300, 300))

        self.curentHpAlier = self.myfont.render(str(self.ChocobosAllier.getPvActuel()), False, (0,0,0))
        self.curentHpEnem = self.myfont.render(str(self.ChocobosEnnemis.getPvActuel()), False, (0,0,0))

        self.MaxHpAllier = self.myfont.render(str(self.ChocobosAllier.getChocobos().getPv()), False, (0,0,0))
        self.MaxHpEnem = self.myfont.render(str(self.ChocobosEnnemis.getChocobos().getPv()), False, (0,0,0))

        self.nomPokeAllier = self.myfont.render(self.ChocobosAllier.getChocobos().getName(), False, (0,0,0))
        self.nomPokeEnemis = self.myfont.render(self.ChocobosEnnemis.getChocobos().getName(), False, (0,0,0))

    # boucle principale

    def load(self):
        if not self.sound:
            self.sound = pygame.mixer.Sound(self.path)

    def boucle_principale(self):
        while self.RUNNING:
            self.fenetre.fill( (255,255,255) )
            self.fenetre.blit(self.bg, (0, 0))
            self.fenetre.blit(self.hudEnemie,(30, 28))
            self.fenetre.blit(self.hudPlayer,(500, 408))
            self.fenetre.blit(self.baseEnemie,(445,185))
            self.fenetre.blit(self.basePlayer,(0,435))
            self.fenetre.blit(self.pokeAllier,(30,268))
            self.fenetre.blit(self.pokeEne,(500,0))
            pygame.draw.rect(self.fenetre,(100,100,100),pygame.Rect(50, 48, 130, 5))
            pygame.draw.rect(self.fenetre,(100,100,100),pygame.Rect(517, 427, 130, 5))
            self.gerer_events_principale()
            self.gererBarVieAllier()
            self.gererBarVieEnemis()
            
            ## Exécute la fonction affecté à afficher (menu/jeu)
            if self.atackOn:
                self.menuAffichageAttaque()
                self.menuAttaque([500, 480, 150, 60],0)
                self.menuAttaque([650, 480, 150, 60],1)
                self.menuAttaque([500, 540, 150, 60],2)
                self.menuAttaque([650, 540, 150, 60],3)
            elif self.equOn:
                self.menuAffichagePoke()
                if self.equ.taille() >= 0:
                    if self.equ.getPokemon(0).getPvActuel() > 0:
                        self.menuPoke([350, 480, 150, 60],0)
                if self.equ.taille() >= 1:
                    if self.equ.getPokemon(1).getPvActuel() > 0:
                        self.menuPoke([500, 480, 150, 60],1)
                if self.equ.taille() >= 2:
                    if self.equ.getPokemon(2).getPvActuel() > 0:
                        self.menuPoke([650, 480, 150, 60],2)
                if self.equ.taille() >= 3:
                    if self.equ.getPokemon(3).getPvActuel() > 0:
                        self.menuPoke([350, 540, 150, 60],3)
                if self.equ.taille() >= 4:
                    if self.equ.getPokemon(4).getPvActuel() > 0:
                        self.menuPoke([500, 540, 150, 60],4)
                if self.equ.taille() >= 5:
                    if self.equ.getPokemon(5).getPvActuel() > 0:
                        self.menuPoke([650, 540, 150, 60],5)
            elif self.objOn:
                self.menuAffichageAttaque()
                self.menuObjet1()
            else:
                self.créerMenu([500, 480, 150, 60],'Attaque')
                self.créerMenu([650, 540, 150, 60],'Fuite')
                self.créerMenu([500, 540, 150, 60],'Objet')
                self.créerMenu([650, 480, 150, 60],'Pokemon')
                self.affichageTexte()
                
    
            self.ChocobosAllier = self.equ.getPokemon(0)
            #pygame.time.delay(500)
            self.Maj()

            #pygame.time.delay(500)
            self.affichageHpAllier()
            #pygame.time.delay(500)
            self.affichageHpEne()
            self.fenetre.blit(self.curentHpAlier, (520,435))
            self.fenetre.blit(self.curentHpEnem, (50,55))
            self.fenetre.blit(self.MaxHpAllier, (545,435))
            self.fenetre.blit(self.MaxHpEnem, (75,55))

            self.fenetre.blit(self.nomPokeAllier, (518, 413))
            self.fenetre.blit(self.nomPokeEnemis, (50, 35))

            pygame.display.update()

            
        pygame.quit()
 

# main provisoir pour tester l'interface rapidement

if __name__ == '__main__':
    a = interfaceGame()
    a.boucle_principale()