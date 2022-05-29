import sys

mn_x = -float('inf')
mn_y = -float('inf')
mx_x = float('inf')
mx_y = float('inf')


def intersectie_x(st, dr):
    global mx_x, mn_x
    if st > mx_x or dr < mn_x:
        return 0
    mn_x = max(st, mn_x)
    mx_x = min(dr, mx_x)


def intersectie_y(st, dr):
    global mx_y, mn_y
    if st > mx_y or dr < mn_y:
        return 0
    mn_y = max(st, mn_y)
    mx_y = min(dr, mx_y)


if __name__ == '__main__':
    vid = False
    n = int(input())
    for _ in range(n):
        (a, b, c) = (int(x) for x in (input().split()))
        if b == 0:
            if a > 0:
                r = intersectie_x(-float('inf'), -c / a)
            else:
                r = intersectie_x(-c / a, float('inf'))
            if r == 0:
                vid = True

        else:
            if b > 0:
                r = intersectie_y(-float('inf'), -c / b)
            else:
                r = intersectie_y(-c / b, float('inf'))
            if r == 0:
                vid = True
    if vid:
        print("VOID")
    elif mx_y != float('inf') and mx_x != float('inf') and mn_x != -float('inf') and mn_y != -float('inf'):
        print("BOUNDED")
    else:
        print("UNBOUNDED")
