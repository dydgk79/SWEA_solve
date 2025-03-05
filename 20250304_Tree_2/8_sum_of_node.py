def post_order(n):
    global node_data
    if n <= N:
        if node_data[n] == 0:
            a = post_order(2*n)
            b = post_order((2*n)+1)
            node_data[n] = a+b
        return node_data[n]
    else:
        return 0


T = int(input())

for test_case in range(1, 1+T):
    N, M, L = map(int, input().split())
    node_data = [0]*(N+1)
    for _ in range(M):
        idx, num_data = map(int, input().split())
        node_data[idx] = num_data
    post_order(1)
    print(f'#{test_case} {node_data[L]}')
