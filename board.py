from random import randint
import pygame as pg # J'ai créé un environnement conda avec python 3.11 pour importer pygame (je comprends rien aux environnements aled T_T)
import collections
from collections import namedtuple
from collections import deque

#PARAMETRES
WHITE = (240, 217, 181) # (Adam) J'ai modifié les couleurs noir et blanc, je pense q'il vaut mieux que ce soit les couleurs des pièces et pas de l'échiquier.
BLACK = (121,85,61) # J'ai pris les couleurs standard sur Chess.com
BOARD_SIZE = 320
CASE_SIZE = 40
running = True

# Je mets temporairement le contenu de affichage.py ici parce que j'ai des problèmes pour appeler les variables

black_pawn = pg.image.load("media/noir_pion.png") # J'ai rajouté les pg.image.load, askip ça permet de convertir l'image en une surface utilisable par pygame
BLACK_PAWN = pg.transform.scale(black_pawn, (CASE_SIZE, CASE_SIZE))

black_rook = pg.image.load("media/noir_tour.png")
BLACK_ROOK = pg.transform.scale(black_rook, (CASE_SIZE, CASE_SIZE))

black_bishop = pg.image.load("media/noir_fou.png")
BLACK_BISHOP = pg.transform.scale(black_bishop, (CASE_SIZE, CASE_SIZE))

black_knight = pg.image.load("media/noir_cavalier.png")
BLACK_KNIGHT = pg.transform.scale(black_knight, (CASE_SIZE, CASE_SIZE))

black_queen = pg.image.load("media/noir_dame.png")
BLACK_QUEEN = pg.transform.scale(black_queen, (CASE_SIZE, CASE_SIZE))

black_king = pg.image.load("media/noir_roi.png")
BLACK_KING = pg.transform.scale(black_king,(CASE_SIZE, CASE_SIZE))

white_pawn = pg.image.load("media/blanc_pion.png")
WHITE_PAWN = pg.transform.scale(white_pawn, (CASE_SIZE, CASE_SIZE))

white_rook = pg.image.load("media/blanc_tour.png")
WHITE_ROOK = pg.transform.scale(white_rook, (CASE_SIZE, CASE_SIZE))

white_bishop = pg.image.load("media/blanc_fou.png")
WHITE_BISHOP = pg.transform.scale(white_bishop, (CASE_SIZE, CASE_SIZE))

white_knight = pg.image.load("media/blanc_cavalier.png")
WHITE_KNIGHT = pg.transform.scale(white_knight, (CASE_SIZE, CASE_SIZE))

white_queen = pg.image.load("media/blanc_dame.png")
WHITE_QUEEN = pg.transform.scale(white_queen, (CASE_SIZE, CASE_SIZE))

white_king = pg.image.load("media/blanc_roi.png")
WHITE_KING = pg.transform.scale(white_king, (CASE_SIZE, CASE_SIZE))

pg.init()
screen = pg.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pg.display.set_caption("Chess")
clock = pg.time.Clock()

screen.fill(WHITE)

for i in range(CASE_SIZE,BOARD_SIZE,2*CASE_SIZE):
    for j in range(0,BOARD_SIZE,2*CASE_SIZE) :
        # les coordonnées de rectangle que l'on dessine
        x = i # coordonnée x (colonnes) en pixels
        y = j # coordonnée y (lignes) en pixels
        rect = pg.Rect(x, y, CASE_SIZE, CASE_SIZE)
        # appel à la méthode draw.rect()
        pg.draw.rect(screen, BLACK, rect)

for i in range(0,BOARD_SIZE,2*CASE_SIZE): 
    for j in range(CASE_SIZE,BOARD_SIZE,2*CASE_SIZE) :
        # les coordonnées de rectangle que l'on dessine
        x = i # coordonnée x (colonnes) en pixels
        y = j # coordonnée y (lignes) en pixels
        rect = pg.Rect(x, y, CASE_SIZE, CASE_SIZE)
        # appel à la méthode draw.rect()
        pg.draw.rect(screen, BLACK, rect)

for i in range(0, BOARD_SIZE, CASE_SIZE):
    screen.blit(WHITE_PAWN, (i, BOARD_SIZE - 2 * CASE_SIZE))
for i in range(0, BOARD_SIZE, CASE_SIZE):
    screen.blit(BLACK_PAWN, (i, CASE_SIZE))

screen.blit(BLACK_ROOK, (0, 0))
screen.blit(BLACK_KNIGHT, (CASE_SIZE, 0))
screen.blit(BLACK_BISHOP, (2 * CASE_SIZE, 0))
screen.blit(BLACK_QUEEN, (3 * CASE_SIZE, 0))
screen.blit(BLACK_KING, (4 * CASE_SIZE, 0))
screen.blit(BLACK_BISHOP, (5 * CASE_SIZE, 0))
screen.blit(BLACK_KNIGHT, (6 * CASE_SIZE, 0))
screen.blit(BLACK_ROOK, (7 * CASE_SIZE, 0))

screen.blit(WHITE_ROOK, (0, BOARD_SIZE - CASE_SIZE))
screen.blit(WHITE_KNIGHT, (CASE_SIZE, BOARD_SIZE - CASE_SIZE))
screen.blit(WHITE_BISHOP, (2 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
screen.blit(WHITE_QUEEN, (3 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
screen.blit(WHITE_KING, (4 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
screen.blit(WHITE_BISHOP, (5 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
screen.blit(WHITE_KNIGHT, (6 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
screen.blit(WHITE_ROOK, (7 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))

while running:
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
    pg.display.update()
pg.quit()


"""
Utilisation de chatgpt pour comprendre certaines fonctions de pygame.
J'ai utilisé pg.display.set_caption, screen.blit, pg.image.load, pg.transform.scale
"""
