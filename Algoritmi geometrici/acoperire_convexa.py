def determinant(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    return a11 * a22 * a33 + a21 * a32 * a13 + a12 * a23 * a31 - a13 * a22 * a31 - a11 * a32 * a23 - a12 * a21 * a33


def test_orientare(ax, ay, bx, by, cx, cy):
    D = determinant(1, 1, 1, ax, bx, cx, ay, by, cy)
    if D == 0:
        return "TOUCH"
    if D < 0:
        return "RIGHT"
    return "LEFT"


class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x} {self.y}"


def grahamScan():
    stiva = [puncte[0], puncte[1]]
    for i in range(2, len(puncte)):
        ultim = stiva[-1]
        penultim = stiva[-2]
        viraj = test_orientare(penultim.x, penultim.y, ultim.x, ultim.y, puncte[i].x, puncte[i].y)
        if viraj == "LEFT":
            stiva.append(puncte[i])
        else:
            while viraj != "LEFT" and len(stiva) > 1:
                stiva.pop()
                if len(stiva) == 1:
                    break
                ultim = stiva[-1]
                penultim = stiva[-2]
                viraj = test_orientare(penultim.x, penultim.y, ultim.x, ultim.y, puncte[i].x, puncte[i].y)
            stiva.append(puncte[i])
    return stiva


def margine_inferioara():
    puncte.sort(key=lambda p: p.x)
    return grahamScan()


def margine_superioara():
    puncte.reverse()
    return grahamScan()


def rezolva():
    i = margine_inferioara()
    s = margine_superioara()
    return i + s[1:-1]


if __name__ == '__main__':
    puncte = []
    acoperire = []
    n = int(input())
    for _ in range(n):
        punct = input().split()
        puncte.append(Punct(int(punct[0]), int(punct[1])))
    r = rezolva()
    print(len(r))
    for p in r:
        print(p)
