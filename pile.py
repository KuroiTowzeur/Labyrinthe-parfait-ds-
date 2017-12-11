class Pile:
    def __init__(self):
        self._content = []
        self.taille = 0

    def depile(self):
        if not (self.estVide()):
            return self._content.pop()
        raise Exception('Impossible de dépiler une pile vide')

    def empile(self, x):
        self._content.append(x)
        self.taille += 1

    def estVide(self):
        return not (self._content)

    def sommet(self):
        if not (self.estVide()):
            return self._content[-1]

    def __str__(self):
        return str(self._content)


