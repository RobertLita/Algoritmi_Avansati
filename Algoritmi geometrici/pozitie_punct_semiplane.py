def f(x, y):
    x_inf = y_inf = -float('inf')
    x_sup = y_sup = float('inf')
    for semiplan in semiplane:
        if semiplan[0] == 0:
            if semiplan[1] > 0:
                if y < - semiplan[2] / semiplan[1]:
                    y_sup = min(y_sup, - semiplan[2] / semiplan[1])
            else:
                if y > - semiplan[2] / semiplan[1]:
                    y_inf = max(y_inf, - semiplan[2] / semiplan[1])
        elif semiplan[1] == 0:
            if semiplan[0] > 0:
                if x < - semiplan[2] / semiplan[0]:
                    x_sup = min(x_sup, - semiplan[2] / semiplan[0])
            else:
                if x > - semiplan[2] / semiplan[0]:
                    x_inf = max(- semiplan[2] / semiplan[0], x_inf)
    if x_inf < x < x_sup and y_inf < y < y_sup and x_inf != -float('inf') and x_sup != float(
            'inf') and y_inf != -float('inf') and y_sup != float('inf'):
        print("YES")
        rez = (x_sup - x_inf) * (y_sup - y_inf)
        if rez % 1 == 0:
            print(int(rez))
        else:
            print(round(rez, 6))
        return
    print("NO")


if __name__ == "__main__":

    semiplane = []
    n = int(input())
    for _ in range(n):
        (a, b, c) = (int(x) for x in (input().split()))
        semiplane.append((a, b, c))
    m = int(input())
    for _ in range(m):
        (x, y) = (float(c) for c in (input().split()))
        f(x, y)
