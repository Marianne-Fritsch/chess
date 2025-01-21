class Piece():

    def __init__(self, name, couleur, position):
        self.name = name
        self.color = couleur
        self.position = position
        # penser au statut d'être mangé ou pas et comment gérer le code

    def affichage(self):
        pass

    def deplacement_autorisé(self, case_souhaitee):
        if self.name == "pawn":
            pass
        if self.name == "bishop":
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
