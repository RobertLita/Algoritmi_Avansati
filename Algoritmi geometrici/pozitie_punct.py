class Punct:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def determinant(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    return a11 * a22 * a33 + a21 * a32 * a13 + a12 * a23 * a31 - a13 * a22 * a31 - a11 * a32 * a23 - a12 * a21 * a33


def criteriul_numeric(A, B, C, D):
    D = -determinant(B.x, B.y, B.x * B.x + B.y * B.y, C.x, C.y, C.x * C.x + C.y * C.y, D.x, D.y, D.x * D.x + D.y * D.y) + \
           determinant(A.x, A.y, A.x * A.x + A.y * A.y, C.x, C.y, C.x * C.x + C.y * C.y, D.x, D.y, D.x * D.x + D.y * D.y) - \
           determinant(A.x, A.y, A.x * A.x + A.y * A.y, B.x, B.y, B.x * B.x + B.y * B.y, D.x, D.y, D.x * D.x + D.y * D.y) + \
           determinant(A.x, A.y, A.x * A.x + A.y * A.y, B.x, B.y, B.x * B.x + B.y * B.y, C.x, C.y, C.x * C.x + C.y * C.y)
    if D == 0:
        return "BOUNDARY"
    if D > 0:
        return "INSIDE"
    return "OUTSIDE"

if __name__ == "__main__":
    A = Punct()
    (A.x, A.y) = (int(x) for x in input().split())
    B = Punct()
    (B.x, B.y) = (int(x) for x in input().split())
    C = Punct()
    (C.x, C.y) = (int(x) for x in input().split())
    n = int(input())
    for _ in range(n):
        P = Punct()
        (P.x, P.y) = (int(x) for x in input().split())
        print(criteriul_numeric(A, B, C, P))