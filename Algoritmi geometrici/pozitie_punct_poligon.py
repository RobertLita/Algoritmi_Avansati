from random import randint


class Punct:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


def determinant(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    return a11 * a22 * a33 + a21 * a32 * a13 + a12 * a23 * a31 - a13 * a22 * a31 - a11 * a32 * a23 - a12 * a21 * a33


def test_orientare(ax, ay, bx, by, cx, cy):
    D = determinant(1, 1, 1, ax, bx, cx, ay, by, cy)
    if D == 0:
        return "TOUCH"
    if D < 0:
        return "RIGHT"
    return "LEFT"


def se_intersecteaza(A, B, C, D):
    ABC = test_orientare(A.x, A.y, B.x, B.y, C.x, C.y)
    ABD = test_orientare(A.x, A.y, B.x, B.y, D.x, D.y)
    CDA = test_orientare(C.x, C.y, D.x, D.y, A.x, A.y)
    CDB = test_orientare(C.x, C.y, D.x, D.y, B.x, B.y)
    if (ABC == "LEFT" and ABD == "RIGHT") or (ABC == "RIGHT" and ABD == "LEFT"):
        if (CDA == "LEFT" and CDB == "RIGHT") or (CDA == "RIGHT" and CDB == "LEFT"):
            return True
    if ABC == "TOUCH" or ABD == "TOUCH" or CDA == "TOUCH" or CDB == "TOUCH":
        return "TOUCH"
    return False


def pozitie_punct(P, poligon):
    for punct in poligon:
        if P == punct:
            return "BOUNDARY"
    M = Punct(randint(1, 1000000000), randint(1, 1000000000))
    intersectii = 0
    P1 = poligon[0]
    for i in range(1, len(poligon)):
        P2 = poligon[i]
        rez = se_intersecteaza(P1, P2, P, M)
        if rez == True:
            intersectii += 1
        if test_orientare(P1.x, P1.y, P.x, P.y, P2.x, P2.y) == "TOUCH":
            if i < len(poligon) - 1:
                P3 = poligon[i + 1]
            else:
                P3 = poligon[0]
            if i > 1:
                P0 = poligon[i - 2]
            else:
                P0 = poligon[len(poligon) - 1]
            if test_orientare(P.x, P.y, P2.x, P2.y, P3.x, P3.y) == test_orientare(P1.x, P1.y, P2.x, P2.y, P3.x,
                                                                                  P3.y) and test_orientare(P.x, P.y,
                                                                                                           P1.x, P1.y,
                                                                                                           P0.x,
                                                                                                           P0.y) == test_orientare(
                    P2.x, P2.y, P1.x, P1.y, P0.x, P0.y):
                return "BOUNDARY"
        if rez == "TOUCH":
            return pozitie_punct(P, poligon)
        P1 = P2
    if intersectii % 2 == 0:
        return "OUTSIDE"
    return "INSIDE"


if __name__ == '__main__':
    poligon = []
    n = int(input())
    for _ in range(n):
        P = Punct()
        (P.x, P.y) = (int(x) for x in input().split())
        poligon.append(P)
    m = int(input())
    poligon.append(poligon[0])
    for _ in range(m):
        P = Punct()
        (P.x, P.y) = (int(x) for x in input().split())
        print(pozitie_punct(P, poligon))
