T = int(input())

for test_case in range(1, 1+T):
    N = int(input())

    a = 0
    while N%2 == 0:
        a += 1
        N /= 2

    b = 0
    while N%3 == 0:
        b += 1
        N /= 3

    c = 0
    while N%5 == 0:
        c += 1
        N /= 5

    d = 0
    while N%7 == 0:
        d += 1
        N /= 7

    e = 0
    while N%11 == 0:
        e += 1
        N /= 11

    print(f'#{test_case} {a} {b} {c} {d} {e}')