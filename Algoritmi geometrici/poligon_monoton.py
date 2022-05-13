class Punct:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def monoton(puncte, xory):
    p_maxim = p_minim = 0
    maxim = -float('inf')
    minim = float('inf')
    for i in range(len(puncte)):
        coordonata = puncte[i].x if xory == 'x' else puncte[i].y
        if coordonata > maxim:
            maxim = coordonata
            p_maxim = i
        if coordonata < minim:
            minim = coordonata
            p_minim = i
    if p_maxim < p_minim:
        lant2 = puncte[p_maxim: p_minim + 1]
        lant1 = puncte[p_minim:] + puncte[:p_maxim + 1]
    else:
        lant1 = puncte[p_minim: p_maxim + 1]
        lant2 = puncte[p_maxim:] + puncte[:p_minim + 1]
    for i in range(len(lant1) - 1):
        coordonata1 = lant1[i + 1].x if xory == 'x' else lant1[i + 1].y
        coordonata2 = lant1[i].x if xory == 'x' else lant1[i].y
        if coordonata1 < coordonata2:
            return False
    for i in range(len(lant2) - 1):
        coordonata1 = lant2[i + 1].x if xory == 'x' else lant2[i + 1].y
        coordonata2 = lant2[i].x if xory == 'x' else lant2[i].y
        if coordonata1 > coordonata2:
            return False
    return True


if __name__ == "__main__":
    puncte = []
    n = int(input())
    for _ in range(n):
        P = Punct()
        (P.x, P.y) = (int(x) for x in input().split())
        puncte.append(P)
    print("YES") if monoton(puncte, 'x') else print("NO")
    print("YES") if monoton(puncte, 'y') else print("NO")