import numpy as np
from random import randint
import pygame as pg  # J'ai créé un environnement conda avec python 3.11 pour importer pygame (je comprends rien aux environnements aled T_T)
import collections
from collections import namedtuple
from collections import deque



WHITE = (
    240,
    217,
    181,
)  # (Adam) J'ai modifié les couleurs noir et blanc, je pense q'il vaut mieux que ce soit les couleurs des pièces et pas de l'échiquier.
BLACK = (121, 85, 61)  # J'ai pris les couleurs standard sur Chess.com
BOARD_SIZE = 320
CASE_SIZE = 40
running = True




# Je mets temporairement le contenu de affichage.py ici parce que j'ai des problèmes pour appeler les variables

black_pawn = pg.image.load(
    "media/noir_pion.png"
)  # J'ai rajouté les pg.image.load, askip ça permet de convertir l'image en une surface utilisable par pygame
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
BLACK_KING = pg.transform.scale(black_king, (CASE_SIZE, CASE_SIZE))

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
SCREEN = pg.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pg.display.set_caption("Chess")
#clock = pg.time.Clock()

#screen.fill(WHITE)
"""
for i in range(CASE_SIZE, BOARD_SIZE, 2 * CASE_SIZE):
    for j in range(0, BOARD_SIZE, 2 * CASE_SIZE):
        # les coordonnées de rectangle que l'on dessine
        x = i  # coordonnée x (colonnes) en pixels
        y = j  # coordonnée y (lignes) en pixels
        rect = pg.Rect(x, y, CASE_SIZE, CASE_SIZE)
        # appel à la méthode draw.rect()
        pg.draw.rect(screen, BLACK, rect)

for i in range(0, BOARD_SIZE, 2 * CASE_SIZE):
    for j in range(CASE_SIZE, BOARD_SIZE, 2 * CASE_SIZE):
        # les coordonnées de rectangle que l'on dessine
        x = i  # coordonnée x (colonnes) en pixels
        y = j  # coordonnée y (lignes) en pixels
        rect = pg.Rect(x, y, CASE_SIZE, CASE_SIZE)
        # appel à la méthode draw.rect()
        pg.draw.rect(screen, BLACK, rect)

#for i in range(0, BOARD_SIZE, CASE_SIZE):
#    screen.blit(WHITE_PAWN, (i, BOARD_SIZE - 2 * CASE_SIZE))
#for i in range(0, BOARD_SIZE, CASE_SIZE):
#    screen.blit(BLACK_PAWN, (i, CASE_SIZE))

#screen.blit(BLACK_ROOK, (0, 0))
#screen.blit(BLACK_KNIGHT, (CASE_SIZE, 0))
#screen.blit(BLACK_BISHOP, (2 * CASE_SIZE, 0))
#screen.blit(BLACK_QUEEN, (3 * CASE_SIZE, 0))
#screen.blit(BLACK_KING, (4 * CASE_SIZE, 0))
#screen.blit(BLACK_BISHOP, (5 * CASE_SIZE, 0))
#screen.blit(BLACK_KNIGHT, (6 * CASE_SIZE, 0))
#screen.blit(BLACK_ROOK, (7 * CASE_SIZE, 0))

#screen.blit(WHITE_ROOK, (0, BOARD_SIZE - CASE_SIZE))
#screen.blit(WHITE_KNIGHT, (CASE_SIZE, BOARD_SIZE - CASE_SIZE))
#screen.blit(WHITE_BISHOP, (2 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
#screen.blit(WHITE_QUEEN, (3 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
#screen.blit(WHITE_KING, (4 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
#screen.blit(WHITE_BISHOP, (5 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
#screen.blit(WHITE_KNIGHT, (6 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))
#screen.blit(WHITE_ROOK, (7 * CASE_SIZE, BOARD_SIZE - CASE_SIZE))

"""


dico_n_p = {1 : BLACK_ROOK, 2 : BLACK_KNIGHT, 3 : BLACK_BISHOP, 4 : BLACK_QUEEN, 5 : BLACK_KING, 6 : BLACK_PAWN, 7 : WHITE_ROOK, 8 : WHITE_KNIGHT, 9 : WHITE_BISHOP, 10 : WHITE_QUEEN, 11 : WHITE_KING, 12 : WHITE_PAWN}
dico_p_n = {BLACK_ROOK : 1, BLACK_KNIGHT : 2, BLACK_BISHOP : 3, BLACK_QUEEN : 4, BLACK_KING : 5, BLACK_PAWN : 6, WHITE_ROOK : 7, WHITE_KNIGHT : 8, WHITE_BISHOP : 9, WHITE_QUEEN : 10, WHITE_KING : 11, WHITE_PAWN : 12}
dico_n_c = {1 : "black", 2 : "black", 3 : "black", 4 : "black", 5 : "black", 6 : "black", 7 : "white", 8 : "white", 9 : "white", 10 : "white", 11 : "white", 12 : "white"}
dico_n_str = {1 : "rook", 2 : "knight", 3 : "bishop", 4 : "queen", 5 : "king", 6 : "pawn", 7 : "rook", 8 : "knight", 9 : "bishop", 10 : "queen", 11 : "king", 12 : "pawn"}


p_c = np.zeros((8,8))
p_c[0][0]=1
p_c[1][0]=2
p_c[2][0]=3
p_c[3][0]=4
p_c[4][0]=5
p_c[5][0]=3
p_c[6][0]=2
p_c[7][0]=1

p_c[0][1]=6
p_c[1][1]=6
p_c[2][1]=6
p_c[3][1]=6
p_c[4][1]=6
p_c[5][1]=6
p_c[6][1]=6
p_c[7][1]=6

p_c[0][6]=12
p_c[1][6]=12
p_c[2][6]=12
p_c[3][6]=12
p_c[4][6]=12
p_c[5][6]=12
p_c[6][6]=12
p_c[7][6]=12

p_c[0][7]=7
p_c[1][7]=8
p_c[2][7]=9
p_c[3][7]=10
p_c[4][7]=11
p_c[5][7]=9
p_c[6][7]=8
p_c[7][7]=7

#while running:
#    for event in pg.event.get():
#        # chaque évênement à un type qui décrit la nature de l'évênement
#        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
#        if event.type == pg.QUIT:
#            running = False
#        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
#        elif event.type == pg.KEYDOWN:
#            # si la touche est "Q" on veut quitter le programme
#            if event.key == pg.K_q:
#                running = False
#        elif event.type == pg.MOUSEBUTTONDOWN:
#            (x, y) = event.pos
#            i, j = (
#                x // CASE_SIZE,
#                y // CASE_SIZE,
#            )  
#            case_souhaitee = Case((i,j))# il s'agit de la case souhaitée (où i est compté horizontalement et j verticalement)
#    pg.display.update()
#pg.quit()




"""
Utilisation de chatgpt pour comprendre certaines fonctions de pygame.
J'ai utilisé pg.display.set_caption, screen.blit, pg.image.load, pg.transform.scale
"""
