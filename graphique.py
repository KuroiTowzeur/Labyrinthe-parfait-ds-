from PIL import Image, ImageFont, ImageDraw


class Grille:
    def __init__(self, n, taille=600, marge=20):

        self.n = n
        self.taille = taille
        self.marge = marge

        self.r = self.taille / self.n

        self.im = Image.new('RGB',
                            (self.taille + self.marge * 2, self.taille + self.marge * 2),
                            (255, 255, 255))
        self.draw = ImageDraw.Draw(self.im)

        for l in range(n + 1):
            p1 = (self.marge, self.marge + (self.r * l))
            p2 = (self.taille + self.marge, self.marge + (self.r * l))

            self.draw.line((p1, p2), fill=0, width=2)
            self.draw.line((p1[::-1], p2[::-1]), fill=0, width=2)

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
        c1 = self.centers[arete[0][0]][arete[0][1]]
        c2 = self.centers[arete[1][0]][arete[1][1]]

        self.draw.line((c1, c2), fill=255, width=3)

    def show(self):
        self.im.show()




