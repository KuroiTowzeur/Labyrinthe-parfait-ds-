from graphique import Grille
from laby import labyrinthe

n = 20

g = Grille(n)
laby = labyrinthe(n)

for arete in laby._content:

    g.drawArete(arete)

g.show()