from board import *


L_b = []
L_w = []

class Position():
    
    def __init__(self, x, y):
        self.x= x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return(self.x,self.y)
    
class Case:
    def __init__(self,position) :#,statut):
        self.position = position #tuple (de 1 à 8, de 1 à 8)
        #self.statut = statut   #dans {"empty","black","white"}
    
    def euhhhh():   #jsp si y a besoin d'une autre fonction enft
        pass

#il faut un dictionnaire qui recense toutes les cases occupées


class Piece():

    def __init__(self, name, color, position):
        self.name = name
        if self.name == "pawn" or self.name == "rook" or self.name == "king":
            self.memory = "Didn't move yet"
        self.color = color
        self.position = position
        # penser au statut d'être mangé ou pas et comment gérer le code
        # est-ce que on gère les effets de bord ? (pour la case souhaitée)
    def affichage(self):
        i,j = self.position
        x,y = i*CASE_SIZE,j*CASE_SIZE
        screen.blit(self.name, (x, y))

    #def __repr__(self):
    #    return(affichage(self.name,self.position))

    def deplacement_autorise(self, case_souhaitee):

        def vect_unit(a,b):
            return ((a.x-b.x)/abs(a.x-b.x), (a.y-b.y)/abs(a.y-b.y))

        if self.name == "pawn":

            def avancer_pion(case_souhaitee): # est-ce que je code ces fontions ici ou en dehors de def deplacement_autorisé ?
                pos = Position(case_souhaitee.position)
                if pos == self.position + Position(0,1) and self.case_autorisee(case_souhaitee):
                    self.memory = "Moved"
                    return True
                return False

            def avancer_2_pion(case_souhaitee):
                pos = Position(case_souhaitee.position)
                if pos == self.position + Position(0,2) and self.case_autorisee(case_souhaitee) and self.case_autorisee(self.position + Position(0,1)) and self.memory == "Didn't move yet":
                    self.memory = "Just moved 2 squares"# Je ne sais pas encore comment implémenter la notion de mémoire pour la prise en passant
                    return True
                return False
                 
            def manger_pion(case_souhaitee):
                haut_droit = self.position + Position(1,1)
                haut_gauche = self.position + Position(-1,1)
                pos = Position(case_souhaitee.position)
                return pos in {haut_droit, haut_gauche} and self.case_autorisee(case_souhaitee)
                    
            def prise_en_passant(case_souhaitee): 
                h,k = self.position
                pos = Position(case_souhaitee.position)
                if self.statut == "white" :
                    return ((case_souhaitee.position==h-1,k-1) and p_c[h-1][k]==6) or (case_souhaitee.position==h+1,k-1) and p_c[h+1][k]==6
                elif self.statut == "black":
                    return ((case_souhaitee.position==h-1,k+1) and p_c[h-1][k]==12) or ((case_souhaitee.position==h+1,k+1) and p_c[h+1][k]==12)


            return avancer_pion(case_souhaitee) or avancer_2_pion(case_souhaitee) or manger_pion(case_souhaitee) or prise_en_passant(case_souhaitee) # Je teste si la case est autorisée dans toutes les sous-fonctions parce que certaines modifient l'état de self.memory

        if self.name == "bishop":

            diagonals = {}
            for i in range(1, BOARD_SIZE):
                haut_droit = self.position + Position(i,i)
                haut_gauche = self.position + Position(-i,i)
                bas_droit = self.position + Position(i,-i)
                bas_gauche = self.position + Position(-i,-i)
                diagonals.update([haut_droit, haut_gauche, bas_droit, bas_gauche])
            pos = Position(case_souhaitee.position)
            if pos in diagonals and self.case_autorisee(case_souhaitee):
                direction = vect_unit(pos, self.position)
                boolean = True
                for k in range(1,abs(pos.x - self.position.x)):
                    h,k = self.position + k * direction
                    if p_c[h][k] != 0:
                        boolean = False
                return boolean

        if self.name == "knight":
            
            cases_possibles = {self.position + Position(1,2), self.position + Position(2,1), self.position + Position(-1,2), self.position + Position(2,-1), self.position + Position(1,-2), self.position + Position(-2,1), self.position + Position(-1,-2), self.position + Position(-2,-1)}
            pos = Position(case_souhaitee.position)
            return (pos in cases_possibles) and self.case_autorisee(case_souhaitee)

        if self.name == "rook":

            rows = {}
            for i in range(1, BOARD_SIZE):
                haut = self.position + Position(0,i)
                bas = self.position + Position(0,-i)
                droite = self.position + Position(i, 0)
                gauche = self.position + Position(-i, 0)
                rows.update([haut, bas, gauche, droite])
            pos = Position(case_souhaitee.position)
            if pos in rows and self.case_autorisee(case_souhaitee):
                direction = vect_unit(case_souhaitee, self.position)
                boolean = True
                if abs(pos.x - self.position.x) != 0:
                    for k in range(1,abs(pos.x - self.position.x)):
                        h,k=self.position + k * direction
                    if p_c[h][k] != 0:
                        boolean = False
                    return boolean
                else : 
                    for k in range(1,abs(pos.x - self.position.x)):
                        n,m = self.position + k * direction
                        if p_c[n][m]!=0:
                            boolean = False
                        return boolean
            #elif case_souhaitee.position[1]==self.position[1]:
            #    if self.statut == "Didn't move yet" and 
            #je n'arrive pas à faire le roque

        if self.name == "queen":

            rows_and_diagonals = {}
            for i in range(1, BOARD_SIZE):
                haut = self.position + Position(0,i)
                bas = self.position + Position(0,-i)
                droite = self.position + Position(i, 0)
                gauche = self.position + Position(-i, 0)
                haut_droit = self.position + Position(i,i)
                haut_gauche = self.position + Position(-i,i)
                bas_droit = self.position + Position(i,-i)
                bas_gauche = self.position + Position(-i,-i)
                rows_and_diagonals.update([haut, bas, droite, gauche, haut_droit, haut_gauche, bas_droit, bas_gauche])
                pos = Position(case_souhaitee.position)
                if pos in rows_and_diagonals and self.case_autorisee(case_souhaitee):
                    direction = vect_unit(pos, self.position)
                    boolean = True
                    if abs(pos.x - self.position.x) != 0:
                        for k in range(1,abs(pos.x - self.position.x)):
                            n,m = self.position + k * direction
                            if p_c[n][m]!=0:
                                    boolean = False
                                    return boolean
                    else : 
                        for k in range(1,abs(pos.x - self.position.x)):
                            n,m = self.position + k * direction
                            if p_c[n][m]!=0:
                                boolean = False
                                return boolean # Peut-être qu'on peut regrouper les fonctions pour rook, bishop et queen, la seule chose qui change c'est l'ensemble qu'on manipule

        if self.name == "king":

            voisinage = {self.position + Position(0,1), self.position + Position(1,1), self.position + Position(1,0), self.position + Position(1,-1), self.position + Position(0,-1), self.position + Position(-1,-1), self.position + Position(-1,0), self.position + Position(-1, 1)}
            pos = Position(case_souhaitee.position)
            if pos in voisinage and self.case_autorisee(case_souhaitee):
                pass # Le roi va être dur à coder, je propose de le faire vers la fin, parce qu'il faut prendre en compte le roque, le pat, les mises en échec, l'échec et mat.
            
    def case_autorisee(self, case_souhaitee): #case_souhaitee doit être de classe Case
        i,j = case_souhaitee.position 
        if p_c[i][j]!=0:
            return True,"empty"
        return dico_n_c[p_c[i][j]] != self.color,"nempty"


        
        
    def deplacement(self):
        if deplacement_autorise(case_souhaitee) and case_autorisee(case_souhaitee)[0]:
            self.position = Position(case_souhaitee.position)
            h,k = case_souhaitee.position
            n,m = self.position
            if case_autorisee(case_souhaitee)[1] == "nempty":
                w = p_c[h][k]
                dico_p_n[case_souhaitee.name]
                p_c[h][k] = p_c[n][m]       #on ajoute la pièce là où on veut la déplacer
                p_c[n][m] = 0       #on la supprime de là où elle était
                if self.color == "black":
                    L_b.append(dico_n_p[w])
                else : 
                    L_w.append(dico_n_p[w])
            else : 
                p_c[h][k]=p_c[n][m]
            pg.display.update()




        # Penser à redemander une case pour l'IA

    def est_mangee(self):
        pass
