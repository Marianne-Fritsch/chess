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

# pg.init()
# screen = pg.display.set_mode((BOARD_SIZE, BOARD_SIZE))
# pg.display.set_caption("Chess")
# clock = pg.time.Clock()


c = 0
running = True


while running:
    b = c
    print(p_c)
    affichage(p_c, SCREEN)
    pg.display.update()
    while b == c : 
        event1 = pg.event.poll()
        if event1.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event1.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event1.key == pg.K_q:
                running = False
        elif event1.type == pg.MOUSEBUTTONDOWN:
            (x, y) = event1.pos
            i, j = (
                x // CASE_SIZE,
                y // CASE_SIZE,
            )  # il s'agit de la pièce souhaitée (où i est compté horizontalement et j verticalement)
            print(i, j)
            p = int(p_c[i][j])
            if p ==0 :
                print("il n'y a pas de pièce à cet emplacement")
            elif (dico_n_c[p] == "black" and c % 2 == 0) or (
                dico_n_c[p] == "white" and c % 2 == 1
            ):
                print("ce n'est pas à cette couleur de jouer")
            else:
                piece = Piece(dico_n_str[p], dico_n_c[p], (i, j))
                d = c
                while c == d : 
                    event2 = pg.event.poll()
                    if event2.type == pg.QUIT:
                        running = False
                    elif event2.type == pg.MOUSEBUTTONDOWN:
                        (w, z) = event2.pos
                        h, k = (w // CASE_SIZE, z // CASE_SIZE)
                        q = int(p_c[h][k])
                        case_souhaitee = Case((h, k))

                        if piece.deplacement_autorise(case_souhaitee):
                            print("piche2")
                            c += 1
                            piece.deplacement(case_souhaitee,p_c)
                            print(f"L_w = {L_w}, L_b = {L_b}")
                        else :
                            break
                        print("poin")
                    pg.display.update()
pg.quit()
