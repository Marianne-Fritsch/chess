#Ceci est l'interface utilisateur
from random import randint
import pygame as pg 
import collections
from collections import namedtuple
from collections import deque

from board import *
from main import *
from piece import *


def affichage(tab):


    screen = pg.display.set_mode((BOARD_SIZE, BOARD_SIZE))
    pg.display.set_caption("Chess")
    clock = pg.time.Clock()

    screen.fill(WHITE)

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

    for i in range(0,BOARD_SIZE,CASE_SIZE):
        for j in range(0,BOARD_SIZE,CASE_SIZE):
            if tab[i][j]==1:
                screen.blit(BLACK_ROOK, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==2:
                screen.blit(BLACK_KNIGHT, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==3 :
                screen.blit(BLACK_BISHOP, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==4 :
                screen.blit(BLACK_QUEEN, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==5 :
                screen.blit(BLACK_KING, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==6 :
                screen.blit(BLACK_PAWN, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==7 :
                screen.blit(WHITE_ROOK, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==8 :
                screen.blit(WHITE_KNIGHT, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==9 :
                screen.blit(WHITE_BISHOP, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==10 :
                screen.blit(WHITE_QUEEN, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==11 :
                screen.blit(WHITE_KING, (i * CASE_SIZE, j * CASE_SIZE))
            elif tab[i][j]==12 :
                screen.blit(WHITE_PAWN, (i * CASE_SIZE, j * CASE_SIZE))


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


