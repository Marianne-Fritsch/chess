from board import *
from piece import *
from interface_utilisateur import *


# on implémente ici la gestion du clic

c = 0
running = True

while running:
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
            if (dico_n_c[p_c[i][j]] == "black" and c % 2 == 0) or (
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
                            x // CASE_SIZE,
                            y // CASE_SIZE,
                        )  # il s'agit maintenant de la case voulue
                        couleur = dico_n_c[p_c[h][k]]
                        case_souhaitee = Case((i, j), couleur)

                        deplacement_autorise(self, case_souhaitee)

                        c += 1
                        print(f"L_w = {L_w}, L_b = {L_b}")
                        affichage(p_c)
    pg.display.update()
pg.quit()
