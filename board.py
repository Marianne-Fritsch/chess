from random import randint
import pygame as pg
import collections
from collections import namedtuple
from collections import deque

#PARAMETRES
white = (255,255,255)
black = (0,0,0)
BOARD_SIZE = 320
CASE_SIZE = 40
running = True

pg.init()
screen = pg.display.set_mode((BOARD_SIZE, BOARD_SIZE))
clock = pg.time.Clock()

screen.fill(white)

for i in range(CASE_SIZE,BOARD_SIZE,2*CASE_SIZE):
    for j in range(0,BOARD_SIZE,2*CASE_SIZE) :
        # les coordonnées de rectangle que l'on dessine
        x = i # coordonnée x (colonnes) en pixels
        y = j # coordonnée y (lignes) en pixels
        rect = pg.Rect(x, y, CASE_SIZE, CASE_SIZE)
        # appel à la méthode draw.rect()
        pg.draw.rect(screen, black, rect)

for i in range(0,BOARD_SIZE,2*CASE_SIZE): 
    for j in range(CASE_SIZE,BOARD_SIZE,2*CASE_SIZE) :
        # les coordonnées de rectangle que l'on dessine
        x = i # coordonnée x (colonnes) en pixels
        y = j # coordonnée y (lignes) en pixels
        rect = pg.Rect(x, y, CASE_SIZE, CASE_SIZE)
        # appel à la méthode draw.rect()
        pg.draw.rect(screen, black, rect)

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
