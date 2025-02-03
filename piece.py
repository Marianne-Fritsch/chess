class Position():
    
    def __init__(self, x, y):
        self.x= x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

class Piece():

    def __init__(self, name, couleur, position):
        self.name = name
        if self.name == "pawn":
            self.memory = "Didn't move yet"
        self.color = couleur
        self.position = position
        # penser au statut d'être mangé ou pas et comment gérer le code
        # est-ce que on gère les effets de bord ? (pour la case souhaitée)
    def affichage(self):
        pass

    def deplacement_autorise(self, case_souhaitee):

        def vect_unit(a,b):
            return ((a.x-b.x)/abs(a.x-b.x), (a.y-b.y)/abs(a.y-b.y))

        if self.name == "pawn":

            def avancer_pion(case_souhaitee): # est-ce que je code ces fontions ici ou en dehors de def deplaceent_autorisé ?
                if case_souhaitee == self.position + Position(0,1) and self.case_autorisee(case_souhaitee):
                    self.memory = "Moved"
                    return True
                return False

            def avancer_2_pion(case_souhaitee):
                if case_souhaitee == self.position + Position(0,2) and self.case_autorisee(case_souhaitee) and self.case_autorisee(self.position + Position(0,1)) and self.memory == "Didn't move yet":
                    self.memory = "Just moved 2 squares"# Je ne sais pas encore comment implémenter la notion de mémoire pour la prise en passant
                    return True
                return False
                 
            def manger_pion(case_souhaitee):
                haut_droit = self.position + Position(1,1)
                haut_gauche = self.position + Position(-1,1)
                return case_souhaitee in {haut_droit, haut_gauche} and self.case_autorisee(case_souhaitee)
                    
            def prise_en_passant(case_souhaitee): 
                pass

            return avancer_pion(case_souhaitee) or avancer_2_pion(case_souhaitee) or manger_pion(case_souhaitee) or prise_en_passant(case_souhaitee) # Je teste si la case est autorisée dans toutes les sous-fonctions parce que certaines modifient l'état de self.memory

        if self.name == "bishop":

            diagonals = {}
            for i in range(1, BOARD_SIZE):
                haut_droit = self.position + Position(i,i)
                haut_gauche = self.position + Position(-i,i)
                bas_droit = self.position + Position(i,-i)
                bas_gauche = self.position + Position(-i,-i)
                diagonals.update([haut_droit, haut_gauche, bas_droit, bas_gauche])
            if case_souhaitee in diagonals and self.case_autorisee(case_souhaitee):
                direction = vect_unit(case_souhaitee, self.position)
                boolean = True
                for k in range(1,abs(case_souhaitee.x - self.position.x)):
                    if statut(self.position + k * direction) != "empty":
                        boolean = False
                return boolean

        if self.name == "knight":
            
            cases_possibles = {self.position + Position(1,2), self.position + Position(2,1), self.position + Position(-1,2), self.position + Position(2,-1), self.position + Position(1,-2), self.position + Position(-2,1), self.position + Position(-1,-2), self.position + Position(-2,-1)}
            return (case_souhaitee in cases_possibles) and self.case_autorisee(case_souhaitee)

        if self.name == "rook":

            rows = {}
            for i in range(1, BOARD_SIZE):
                haut = self.position + Position(0,i)
                bas = self.position + Position(0,-i)
                droite = self.position + Position(i, 0)
                gauche = self.position + Position(-i, 0)
                rows.update([haut, bas, gauche, droite])
            if case_souhaitee in rows and self.case_autorisee(case_souhaitee):
                direction = vect_unit(case_souhaitee, self.position)
                boolean = True
                if abs(case_souhaitee.x - self.position.x) != 0:
                    for k in range(1, abs(case_souhaitee.x - self.position.x)):
                        if statut(self.position + k * direction) != "empty":
                            boolean = False
                        return boolean
                else : 
                    for k in range(1, abs(case_souhaitee.y - self.position.y)):
                        if statut(self.position + k * direction) != "empty":
                            boolean = False
                        return boolean


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
                if case_souhaitee in rows_and_diagonals and self.case_autorisee(case_souhaitee):
                    direction = vect_unit(case_souhaitee, self.position)
                    boolean = True
                    if abs(case_souhaitee.x - self.position.x) != 0:
                        for k in range(1, abs(case_souhaitee.x - self.position.x)):
                            if statut(self.position + k * direction) != "empty":
                                boolean = False
                            return boolean
                    else : 
                        for k in range(1, abs(case_souhaitee.y - self.position.y)):
                            if statut(self.position + k * direction) != "empty":
                                boolean = False
                            return boolean # Peut-être qu'on peut regrouper les fonctions pour rook, bishop et queen, la seule chose qui change c'est l'ensemble qu'on manipule

        if self.name == "king":

            voisinage = {self.position + Position(0,1), self.position + Position(1,1), self.position + Position(1,0), self.position + Position(1,-1), self.position + Position(0,-1), self.position + Position(-1,-1), self.position + Position(-1,0), self.position + Position(-1, 1)}
            if case_souhaitee in voisinage and self.case_autorisee(case_souhaitee):
                pass # Le roi va être dur à coder, je propose de le faire vers la fin, parce qu'il faut prendre en compte le roque, le pat, les mises en échec, l'échec et mat.
            
    def case_autorisee(self, case_souhaitee):
        if statut(case_souhaitee) == "empty":
            return True
        return statut(case_souhaitee) != self.color

        
        
    def deplacement(self):
        if deplacement_autorise(case_souhaitee) and case_autorisee(case_souhaitee):
            self.position = case_souhaitee
        # Penser à redemander une case pour l'IA

    def est_mangee(self):
        pass
