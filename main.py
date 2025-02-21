from board import *
from piece import *


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
        elif event.type == pg.MOUSEBUTTONDOWN:
            (x, y) = event.pos
            i, j = (
                x // CASE_SIZE,
                y // CASE_SIZE,
            )  # il s'agit de la case souhaitée (où i est compté horizontalement et j verticalement)
            case_souhaitee = 
    pg.display.update()
pg.quit()