import pygame as pg
from board import * # C'est risqué mais j'ai besoin de CASE_SIZE

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



