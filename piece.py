import numpy as np
from random import randint
import pygame as pg  # J'ai créé un environnement conda avec python 3.11 pour importer pygame (je comprends rien aux environnements aled T_T)
import collections
from collections import namedtuple
from collections import deque

from board import *

WHITE = (
    240,
    217,
    181,
)  # (Adam) J'ai modifié les couleurs noir et blanc, je pense q'il vaut mieux que ce soit les couleurs des pièces et pas de l'échiquier.
BLACK = (121, 85, 61)  # J'ai pris les couleurs standard sur Chess.com
BOARD_SIZE = 320
CASE_SIZE = 40


L_b = []
L_w = []


p_c = np.zeros((8, 8))
p_c[0][0] = 1
p_c[1][0] = 2
p_c[2][0] = 3
p_c[3][0] = 4
p_c[4][0] = 5
p_c[5][0] = 3
p_c[6][0] = 2
p_c[7][0] = 1

p_c[0][1] = 6
p_c[1][1] = 6
p_c[2][1] = 6
p_c[3][1] = 6
p_c[4][1] = 6
p_c[5][1] = 6
p_c[6][1] = 6
p_c[7][1] = 6

p_c[0][6] = 12
p_c[1][6] = 12
p_c[2][6] = 12
p_c[3][6] = 12
p_c[4][6] = 12
p_c[5][6] = 12
p_c[6][6] = 12
p_c[7][6] = 12

p_c[0][7] = 7
p_c[1][7] = 8
p_c[2][7] = 9
p_c[3][7] = 10
p_c[4][7] = 11
p_c[5][7] = 9
p_c[6][7] = 8
p_c[7][7] = 7


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def mul(self, k):
        return Position(k * self.x, k * self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Case:
    def __init__(self, position):  # ,statut):
        self.position = position  # tuple (de 1 à 8, de 1 à 8)
        # self.statut = statut   #dans {"empty","black","white"}


# il faut un dictionnaire qui recense toutes les cases occupées


class Piece:
    def __init__(self, name, color, position):
        self.name = name
        if self.name == "pawn" or self.name == "rook" or self.name == "king":
            self.memory = "Didn't move yet"
        self.color = color
        self.position = position
        # penser au statut d'être mangé ou pas et comment gérer le code
        # est-ce que on gère les effets de bord ? (pour la case souhaitée)

    # def affichage(self):
    #    i, j = self.position
    #    x, y = i * CASE_SIZE, j * CASE_SIZE
    #    screen.blit(self.name, (x, y))

    # def __repr__(self):
    #    return(affichage(self.name,self.position))

    def deplacement_autorise(self, case_souhaitee):
        def vect_unit(a, b):
            return Position((a.x - b.x) / abs(a.x - b.x), (a.y - b.y) / abs(a.y - b.y))

        if self.name == "pawn":

            def avancer_pion(
                case_souhaitee,
            ):  # est-ce que je code ces fontions ici ou en dehors de def deplacement_autorisé ?
                pos = Position(*case_souhaitee.position)
                p = int(p_c[Position(*self.position).x][Position(*self.position).y])
                if p != 0:
                    if dico_n_c[p] == "white":
                        print(pos)
                        print(Position(*self.position) + Position(0, -1))
                        if bool(
                            str(pos) == str(Position(*self.position) + Position(0, -1))
                        ) and bool(self.case_autorisee(case_souhaitee)):
                            self.memory = "Moved"
                            print("coucou")
                            return True
                        return False
                    else:
                        print(pos)
                        print(Position(*self.position) + Position(0, 1))
                        if bool(
                            str(pos) == str(Position(*self.position) + Position(0, 1))
                        ) and bool(self.case_autorisee(case_souhaitee)):
                            self.memory = "Moved"
                            print(self.memory)
                            return True
                        return False

            def avancer_2_pion(case_souhaitee):
                pos = Position(*case_souhaitee.position)
                if (
                    str(pos) == str(Position(*self.position) + Position(0, 2))
                    and bool(self.case_autorisee(case_souhaitee))
                    and bool(
                        self.case_autorisee(Position(*self.position) + Position(0, 1))
                    )
                    and bool(self.memory == "Didn't move yet")
                ):
                    self.memory = "Just moved 2 squares"  # Je ne sais pas encore comment implémenter la notion de mémoire pour la prise en passant
                    return True
                return False

            def manger_pion(case_souhaitee):
                haut_droit = str(Position(*self.position) + Position(1, 1))
                haut_gauche = str(Position(*self.position) + Position(-1, 1))
                pos = Position(*case_souhaitee.position)
                return str(pos) in {haut_droit, haut_gauche} and bool(
                    self.case_autorisee(case_souhaitee)
                )

            def prise_en_passant(case_souhaitee):
                h, k = self.position
                pos = Position(*case_souhaitee.position)
                p = int(p_c[h][k])
                if dico_n_c[p] == "white":
                    return (
                        (
                            (case_souhaitee.position == h - 1, k - 1)
                            and h - 1 >= 0
                            and p_c[h - 1][k] == 6
                        )
                        or (case_souhaitee.position == h + 1, k - 1)
                        and h + 1 < 8
                        and p_c[h + 1][k] == 6
                    )
                elif dico_n_c[p] == "black":
                    return (
                        (case_souhaitee.position == h - 1, k + 1)
                        and p_c[h - 1][k] == 12
                    ) or (
                        (case_souhaitee.position == h + 1, k + 1)
                        and p_c[h + 1][k] == 12
                    )

            return (
                avancer_pion(case_souhaitee)
                or avancer_2_pion(case_souhaitee)
                or manger_pion(case_souhaitee)
                or prise_en_passant(case_souhaitee)
            )  # Je teste si la case est autorisée dans toutes les sous-fonctions parce que certaines modifient l'état de self.memory

        if self.name == "bishop":
            diagonals = set()
            for i in range(1, BOARD_SIZE):
                haut_droit = str(Position(*self.position) + Position(i, i))
                haut_gauche = str(Position(*self.position) + Position(-i, i))
                bas_droit = str(Position(*self.position) + Position(i, -i))
                bas_gauche = str(Position(*self.position) + Position(-i, -i))
                diagonals.update([haut_droit, haut_gauche, bas_droit, bas_gauche])
            pos = Position(*case_souhaitee.position)
            if str(pos) in diagonals and bool(self.case_autorisee(case_souhaitee)):
                direction = vect_unit(pos, self.position)
                boolean = True
                for k in range(1, abs(pos.x - Position(*self.position).x)):
                    n, m = (
                        (Position(*self.position) + direction.mul(k)).x,
                        (Position(*self.position) + direction.mul(k)).y,
                    )
                    if p_c[n][m] != 0:
                        boolean = False
                return boolean

        if self.name == "knight":
            cases_possibles = set()
            cases_possibles.update(
                [
                    str(Position(*self.position) + Position(1, 2)),
                    str(Position(*self.position) + Position(2, 1)),
                    str(Position(*self.position) + Position(-1, 2)),
                    str(Position(*self.position) + Position(2, -1)),
                    str(Position(*self.position) + Position(1, -2)),
                    str(Position(*self.position) + Position(-2, 1)),
                    str(Position(*self.position) + Position(-1, -2)),
                    str(Position(*self.position) + Position(-2, -1)),
                ]
            )
            pos = Position(*case_souhaitee.position)
            print(
                bool(str(pos) in list(cases_possibles)),
                bool(self.case_autorisee(case_souhaitee)),
            )
            return bool(str(pos) in cases_possibles) and bool(
                self.case_autorisee(case_souhaitee)
            )

        if self.name == "rook":
            rows = set()
            for i in range(1, BOARD_SIZE):
                haut = str(Position(*self.position) + Position(0, i))
                bas = str(Position(*self.position) + Position(0, -i))
                droite = str(Position(*self.position) + Position(i, 0))
                gauche = str(Position(*self.position) + Position(-i, 0))
                rows.update([haut, bas, gauche, droite])
            pos = Position(*case_souhaitee.position)
            if str(pos) in rows and bool(self.case_autorisee(case_souhaitee)):
                direction = vect_unit(case_souhaitee, self.position)
                boolean = True
                if abs(pos.x - Position(*self.position).x) != 0:
                    for k in range(1, abs(pos.x - Position(*self.position).x)):
                        n, m = (
                            (Position(*self.position) + direction.mul(k)).x,
                            (Position(*self.position) + direction.mul(k)).y,
                        )
                    if p_c[n][m] != 0:
                        boolean = False
                    return boolean
                else:
                    for k in range(1, abs(pos.y - Position(*self.position).y)):
                        n, m = (
                            (Position(*self.position) + direction.mul(k)).x,
                            (Position(*self.position) + direction.mul(k)).y,
                        )
                        if p_c[n][m] != 0:
                            boolean = False
                        return boolean
            # elif case_souhaitee.position[1]==self.position[1]:
            #    if self.statut == "Didn't move yet" and
            # je n'arrive pas à faire le roque

        if self.name == "queen":
            rows_and_diagonals = set()
            for i in range(1, BOARD_SIZE):
                haut = str(Position(*self.position) + Position(0, i))
                bas = str(Position(*self.position) + Position(0, -i))
                droite = str(Position(*self.position) + Position(i, 0))
                gauche = str(Position(*self.position) + Position(-i, 0))
                haut_droit = str(Position(*self.position) + Position(i, i))
                haut_gauche = str(Position(*self.position) + Position(-i, i))
                bas_droit = str(Position(*self.position) + Position(i, -i))
                bas_gauche = str(Position(*self.position) + Position(-i, -i))
                rows_and_diagonals.update(
                    [
                        haut,
                        bas,
                        droite,
                        gauche,
                        haut_droit,
                        haut_gauche,
                        bas_droit,
                        bas_gauche,
                    ]
                )
                pos = Position(*case_souhaitee.position)
                if str(pos) in rows_and_diagonals and bool(
                    self.case_autorisee(case_souhaitee)
                ):
                    direction = vect_unit(pos, self.position)
                    boolean = True
                    if abs(pos.x - Position(*self.position).x) != 0:
                        for k in range(1, abs(pos.x - Position(*self.position).x)):
                            n, m = (
                                (Position(*self.position) + direction.mul(k)).x,
                                (Position(*self.position) + direction.mul(k)).y,
                            )
                            if p_c[n][m] != 0:
                                boolean = False
                                return boolean
                    else:
                        for k in range(1, abs(pos.y - Position(*self.position).y)):
                            n, m = (
                                (Position(*self.position) + direction.mul(k)).x,
                                (Position(*self.position) + direction.mul(k)).y,
                            )
                            if p_c[n][m] != 0:
                                boolean = False
                                return boolean  # Peut-être qu'on peut regrouper les fonctions pour rook, bishop et queen, la seule chose qui change c'est l'ensemble qu'on manipule

        if self.name == "king":
            voisinage = {
                str(Position(*self.position) + Position(0, 1)),
                str(Position(*self.position) + Position(1, 1)),
                str(Position(*self.position) + Position(1, 0)),
                str(Position(*self.position) + Position(1, -1)),
                str(Position(*self.position) + Position(0, -1)),
                str(Position(*self.position) + Position(-1, -1)),
                str(Position(*self.position) + Position(-1, 0)),
                str(Position(*self.position) + Position(-1, 1)),
            }
            pos = Position(*case_souhaitee.position)
            if str(pos) in voisinage and bool(self.case_autorisee(case_souhaitee)):
                pass  # Le roi va être dur à coder, je propose de le faire vers la fin, parce qu'il faut prendre en compte le roque, le pat, les mises en échec, l'échec et mat.

    def case_autorisee(self, case_souhaitee):  # case_souhaitee doit être de classe Case
        i = case_souhaitee.position[0]
        j = case_souhaitee.position[1]
        if int(p_c[i][j]) == 0:
            return True
        p = int(p_c[i][j])
        return dico_n_c[p] != self.color

    def deplacement(self, case_souhaitee, tab):
        # if bool(self.deplacement_autorise(case_souhaitee)) and bool(self.case_autorisee(
        #    case_souhaitee
        # )):

        h,k = case_souhaitee.position[0], case_souhaitee.position[1]
        n,m = int(Position(*self.position).x), int(Position(*self.position).y)
        if int(tab[h][k]) != 0:
            p = int(tab[h][k])
            tab[h][k] = tab[n][m]  # on ajoute la pièce là où on veut la déplacer
            tab[n][m] = 0  # on la supprime de là où elle était
            if self.color == "black":
                L_b.append(dico_n_p[p])
            else:
                L_w.append(dico_n_p[p])
        else:
            a = int(tab[n][m])
            tab[n][m] = 0
            tab[h][k] = a
            print(tab, "hihiha",n,m,h,k)
            # pg.display.update()

        # Penser à redemander une case pour l'IA
