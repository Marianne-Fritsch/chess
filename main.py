from piece import *
from interface_utilisateur import *
from board import *


import numpy as np
from random import randint
import pygame as pg  # J'ai créé un environnement conda avec python 3.11 pour importer pygame (je comprends rien aux environnements aled T_T)
import collections
from collections import namedtuple
from collections import deque




# on implémente ici la gestion du clic

#pg.init()
#screen = pg.display.set_mode((BOARD_SIZE, BOARD_SIZE))
#pg.display.set_caption("Chess")
clock = pg.time.Clock()


c = 0
running = True

while running:
    clock.tick(0.4)

    affichage(p_c,SCREEN)
    for event in pg.event.get():
        # chaque événement à un type qui décrit la nature de l'événement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            (x, y) = event.pos
            print("huhu")
            i, j = (
                x // CASE_SIZE,
                y // CASE_SIZE,
            )  # il s'agit de la pièce souhaitée (où i est compté horizontalement et j verticalement)
            if p_c[i][j] == 0:
                break
            elif (dico_n_c[p_c[i][j]] == "black" and c % 2 == 0) or (
                dico_n_c[p_c[i][j]] == "white" and c % 2 == 1
            ):
                print("ce n'est pas à cette couleur de jouer")
                break
            else:
                piece = Piece(dico_n_str[p_c[i][j]], dico_n_c[p_c[i][j]], (i, j))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        (w, z) = event.pos
                        h, k = (
                            w // CASE_SIZE,
                            z // CASE_SIZE,
                        )  # il s'agit maintenant de la case voulue
                        couleur = dico_n_c[p_c[h][k]]
                        case_souhaitee = Case((i, j))

                        if piece.deplacement_autorise(case_souhaitee):
                            c += 1
                            deplacement(piece, case_souhaitee)
                            print(f"L_w = {L_w}, L_b = {L_b}")
                pg.display.update()
pg.quit()
