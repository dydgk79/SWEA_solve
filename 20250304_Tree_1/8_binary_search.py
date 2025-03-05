def in_order(t):
    global tree
    global k
    if t <= N:
        in_order(2*t)
        tree[t] = k
        k += 1
        in_order(2*t+1)


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    k = 1
    tree = [0]*(N+1)
    in_order(1)
    print(f'#{test_case} {tree[1]} {tree[N//2]}')

