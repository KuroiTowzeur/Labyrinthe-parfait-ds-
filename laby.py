import random
from pile import Pile
from pprint import pprint

initLaby = lambda n, b: [[b for c in range(n)] for l in range(n)]


def labyrinthe(n):
    atteint = initLaby(n, False)

    p = Pile()

    laby = Pile()
    c = (0, 0)
    #
    p.empile(c)

    atteint = visiter(c, atteint)

    while not (p.estVide()):

        c = p.depile()
        v = voisins(c, atteint)

        if v:
            s = choisir(v)
            laby.empile((c, s))
            p.empile(c)
            p.empile(s)

            atteint = visiter(s, atteint)

    return laby


# 2
def visiter(c, grille):
    grille[c[0]][c[1]] = True
    return grille


# 3
def deja_visite(c, grille):
    return grille[c[0]][c[1]]


# 4
def voisins(c, grille):
    n = len(grille)
    tmp = initLaby(n + 2, True)

    for i in range(n):
        for y in range(n):
            tmp[i + 1][y + 1] = grille[i][y]

    x, y = c[0] + 1, c[1] + 1

    voisinsArray = [(x - 1, y),  # gauche
                    (x + 1, y),  # droite
                    (x, y - 1),  # haut
                    (x, y + 1)]  # bas

    return [(v[0] - 1, v[1] - 1) for v in voisinsArray if not (deja_visite(v, tmp))]


# 5
def choisir(voisins):
    return random.choice(voisins)


if __name__ == '__main__':
    laby = labyrinthe(10)
    
    print(laby._content)
