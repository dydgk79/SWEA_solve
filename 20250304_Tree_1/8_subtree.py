def pre_order(n):
    global cnt
    if n:
        cnt += 1
        pre_order(left[n])
        pre_order(right[n])


T = int(input())

for test_case in range(1,1+T):
    E, N = map(int, input().split())
    node_data = list(map(int, input().split()))
    left = [0]*(E+2)
    right = [0]*(E+2)
    for idx in range(E):
        p = node_data[idx*2]
        c = node_data[idx*2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    cnt = 0
    pre_order(N)
    print(f'#{test_case} {cnt}')
