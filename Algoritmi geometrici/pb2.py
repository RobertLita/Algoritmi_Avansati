vd = vs = col = 0


def determinant(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    return a11 * a22 * a33 + a21 * a32 * a13 + a12 * a23 * a31 - a13 * a22 * a31 - a11 * a32 * a23 - a12 * a21 * a33


def test_orientare(ax, ay, bx, by, cx, cy):
    global col, vs, vd
    D = determinant(1, 1, 1, ax, bx, cx, ay, by, cy)
    if D == 0:
        col += 1
    elif D < 0:
        vd += 1
    else:
        vs += 1


if __name__ == '__main__':
    n = int(input())
    (ax, ay) = (int(x) for x in input().split())
    (px, py) = (ax, ay)
    (bx, by) = (int(x) for x in input().split())
    for _ in range(n - 2):
        (cx, cy) = (int(x) for x in input().split())
        test_orientare(ax, ay, bx, by, cx, cy)
        (ax, ay) = (bx, by)
        (bx, by) = (cx, cy)
    test_orientare(ax, ay, bx, by, px, py)
    print(vs, vd, col, sep=' ')
