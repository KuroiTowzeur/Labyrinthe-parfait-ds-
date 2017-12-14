from PIL import Image, ImageDraw


class Grille:
    def __init__(self, n, taille=600, marge=20, wallWidth=3):

        self.n = n
        self.taille = taille
        self.marge = marge
        self.wallWidth = wallWidth

        self.r = self.taille / self.n

        self.im = Image.new('RGB',
                            (self.taille + self.marge * 2, self.taille + self.marge * 2),
                            (255, 255, 255))
        self.draw = ImageDraw.Draw(self.im)

        for l in range(n + 1):
            p1 = (self.marge, self.marge + (self.r * l))
            p2 = (self.taille + self.marge, self.marge + (self.r * l))

            self.draw.line((p1, p2), fill=0, width=self.wallWidth)
            self.draw.line((p1[::-1], p2[::-1]), fill=0, width=self.wallWidth)

        self.makeCoord()

    def makeCoord(self):
        '''construit un tableau de taille n n qui contient les coordonnées des centres des cases'''
        self.centers = [[(0, 0) for i in range(self.n)] for i in range(self.n)]

        for l in range(self.n):
            for c in range(self.n):
                center = (self.marge + self.r * (c + 0.5),
                          self.marge + self.r * (l + 0.5))
                self.centers[l][c] = center

                self.draw.point(center, fill=0)

    def drawArete(self, arete):

        k = (self.r / 2) - self.wallWidth + 1

        pr = self.posRelative(arete)

        c1x, c1y = self.centers[arete[0][0]][arete[0][1]]
        c2x, c2y = self.centers[arete[1][0]][arete[1][1]]

        if pr == 'b' or pr == 'g':
            c1x += -k
            c1y += -k
            c2x += +k
            c2y += +k

        elif pr == 'h' or pr == 'd':
            c1x += +k
            c1y += +k
            c2x += -k
            c2y += -k

        self.draw.rectangle((c1x, c1y, c2x, c2y), fill=(255, 255, 255))

    def drawPath(self, path):

        k = (self.r / 2) - self.wallWidth*2 + 1

        n = len(path)


        progression = 156 / (n - 1)

        for i in range(n - 1):

            c1x, c1y = self.centers[path[i][0]][path[i][1]]
            c2x, c2y = self.centers[path[i + 1][0]][path[i + 1][1]]

            pr = self.posRelative(((c1x, c1y), (c2x, c2y)))

            if pr == 'b' or pr == 'g':
                c1x += -k
                c1y += -k
                c2x += +k
                c2y += +k

            elif pr == 'h' or pr == 'd':
                c1x += +k
                c1y += +k
                c2x += -k
                c2y += -k

            color = (round(256 - progression * i),
                     round(100 + progression * i),
                     0)

            self.draw.rectangle((c1x, c1y, c2x, c2y), fill=color)

    def posRelative(self, arete):

        c1x, c1y = arete[0]
        c2x, c2y = arete[1]

        if c1x < c2x:  # gauche
            return 'g'
        elif c1x > c2x:  # droite
            return 'd'
        elif c1y < c2y:  # bas
            return 'b'
        else:  # haut
            return 'h'

    def show(self):
        self.im.show()
