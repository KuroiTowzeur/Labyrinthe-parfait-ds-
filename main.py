from graphique import Grille
from laby import labyrinthe

n = 10

g = Grille(n)
laby = labyrinthe(n)

for arete in laby._content:

    g.drawArete(arete)


g.show()