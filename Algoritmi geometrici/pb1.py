def determinant(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    return a11 * a22 * a33 + a21 * a32 * a13 + a12 * a23 * a31 - a13 * a22 * a31 - a11 * a32 * a23 - a12 * a21 * a33


def test_orientare(ax, ay, bx, by, cx, cy):
    D = determinant(1, 1, 1, ax, bx, cx, ay, by, cy)
    if D == 0:
        return "TOUCH"
    if D < 0:
        return "RIGHT"
    return "LEFT"


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        coordonate_puncte = input().split()
        (ax, ay, bx, by, cx, cy) = (int(c) for c in coordonate_puncte)
        print(test_orientare(ax, ay, bx, by, cx, cy))
