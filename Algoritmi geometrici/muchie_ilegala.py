class Punct:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def determinant(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    return a11 * a22 * a33 + a21 * a32 * a13 + a12 * a23 * a31 - a13 * a22 * a31 - a11 * a32 * a23 - a12 * a21 * a33


def criteriul_numeric(A, B, C, D):
    return -determinant(B.x, B.y, B.x * B.x + B.y * B.y, C.x, C.y, C.x * C.x + C.y * C.y, D.x, D.y, D.x * D.x + D.y * D.y) + \
           determinant(A.x, A.y, A.x * A.x + A.y * A.y, C.x, C.y, C.x * C.x + C.y * C.y, D.x, D.y, D.x * D.x + D.y * D.y) - \
           determinant(A.x, A.y, A.x * A.x + A.y * A.y, B.x, B.y, B.x * B.x + B.y * B.y, D.x, D.y, D.x * D.x + D.y * D.y) + \
           determinant(A.x, A.y, A.x * A.x + A.y * A.y, B.x, B.y, B.x * B.x + B.y * B.y, C.x, C.y, C.x * C.x + C.y * C.y)


if __name__ == '__main__':
    puncte = []
    for _ in range(4):
        P = Punct()
        (P.x, P.y) = (int(x) for x in input().split())
        puncte.append(P)
    if criteriul_numeric(puncte[0], puncte[1], puncte[2], puncte[3]) > 0:
        print("AC: ILLEGAL")
    else:
        print("AC: LEGAL")
    if criteriul_numeric(puncte[1], puncte[2], puncte[3], puncte[0]) > 0:
        print("BD: ILLEGAL")
    else:
        print("BD: LEGAL")
