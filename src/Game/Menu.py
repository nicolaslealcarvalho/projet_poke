import pygame
from InterfaceGame import *
 
pygame.init()
pygame.font.init()
 
RUNNINGS = True
 
fenetre = pygame.display.set_mode((768,300))
 
myfont = pygame.font.SysFont('Helvetic', 20)
 
bg = pygame.image.load("assets/textures/hud/main_screen.png")
 
def gerer_events_principale():
    global RUNNINGS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNINGS = False
 
def menu():
    rect = pygame.draw.rect(
        fenetre,
        (100,100,100),
        pygame.Rect(280, 200, 200, 100))
 
    text = myfont.render('Lancer jeu', False, (200,200,200))
    fenetre.blit(text, (350,245))
 
    gerer_mouse_menu(rect)
     

 
def gerer_mouse_menu(rectangle):
    global afficher
     
    mouse = pygame.mouse.get_pressed()
    if mouse[0]: # UP
        mouse_pos = pygame.mouse.get_pos()
         
        if rectangle.collidepoint(mouse_pos):
            print('Cliqué sur:', rectangle)
            
            # faire le lancement du jeu
            RUNNINGS = False
            a = interfaceGame()
            a.boucle_principale()
 
## Affecte la fonction menu
afficher = menu
 
def boucle_principale():
    while RUNNINGS:
        fenetre.fill( (0,0,0) )
        fenetre.blit(bg, (0, 0))
        gerer_events_principale()
         
        ## Exécute la fonction affecté à afficher (menu/jeu)
        afficher()

        pygame.display.update()
         
    pygame.quit()
 
 
 
boucle_principale()