from graphique import Grille
from laby import labyrinthe

n = 20

g = Grille(n)

dst = (n - 1, n - 1)
laby, path = labyrinthe(n, dst)

for arete in laby._content:
    g.drawArete(arete)

g.drawPath(path)

g.show()
