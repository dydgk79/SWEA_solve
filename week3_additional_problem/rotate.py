T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    input_arr = [list(input().split()) for _ in range(N)]
    deg_90 = list([0]*N for _ in range(N))
    deg_180 = list([0] * N for _ in range(N))
    deg_270 = list([0] * N for _ in range(N))

    print(f'#{test_case}')
    for r in range(N):
        for c in range(N):
            deg_90[r][c] = input_arr[N-1-c][r]
            deg_180[r][c] = input_arr[N-1-r][N-1-c]
            deg_270[r][c] = input_arr[c][N-1-r]

    for r in range(N):
        print("".join(deg_90[r]), end=" ")
        print("".join(deg_180[r]), end=" ")
        print("".join(deg_270[r]))