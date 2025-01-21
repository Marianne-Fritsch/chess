class Piece():

    def __init__(self, name, couleur, position):
        self.name = name
        self.color = couleur
        self.position = position
        # penser au statut d'être mangé ou pas et comment gérer le code
        # est-ce que on gère les effets de bord ? (pour la case souhaitée)
    def affichage(self):
        pass

    def deplacement_autorisé(self, case_souhaitee):
        if self.name == "pawn":

            def avancer_pion(case_souhaitee): # est-ce que je code ces fontions ici ou en dehors de def deplaceent_autorisé ?
                if case_souhaitee == self.position + (0,1): # notions de coordonnée à définir (un peu comme pour le snake, idéalement avec une classe dédiée)
                    return True
                
            def manger_pion(case_souhaitee):
                haut_droit = self.position + (1,1)
                haut_gauche = self.position + (-1,1)
                if case_souhaite in {haut_droit, haut_gauche} and statut(case_souhaitee) not in {"empty", self.color}:
                    return True
                else:
                    return False
            
            def prise_en_passant(case_souhaitee): 
                pass # à compléter

        if self.name == "bishop":

            diagonales = {}
            for i in range(BOARD_SIZE):
                haut_droit = self.position + (i,i)
                haut_gauche = self.position + (-i,i)
                bas_droit = self.position + (i,-i)
                bas_gauche = self.position + (-i,-i)
                diagonales.update([haut_droit, haut_gauche, bas_droit, bas_gauche])
            if case_souhaitee in diagonales:
                if case_souhaitee == self.position: # on sépare ce cas pour ne pas diviser par 0 juste après
                    return False
                else:
                    def vect_unit(a,b):
                        return ((a.x-b.x)/abs(a.x-b.x), (a.y-b.y)/abs(a.y-b.y))
                    direction = vect_unit(case_souhaitee, self.position)
                    boolean = True
                    for k in range(BOARD_SIZE):
                        pass


        if self.name == "knight":
            pass
        if self.name == "rook":
            pass
        if self.name == "queen":
            pass
        if self.name == "king":
            pass

    def case_autorisée(self, case_souhaitee):
        if statut(case_souhaitée) == "empty":
            return True
        elif statut(case_souhaitée) == self.color:
            return False
        else : 
            return True
        
    def deplacement(self):
        if deplacement_autorisé(case_souhaitee) and case_autorisée(case_souhaitee):
            self.position = case_souhaitee
        # Penser à redemander une case pour l'IA

    def est_mangée(self):
        pass
