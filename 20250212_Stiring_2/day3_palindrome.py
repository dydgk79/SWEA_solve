T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    input_arr = list(input() for _ in range(N))

    for r in range(N):
        for c in range(N-M+1):
            for idx_r in range(M//2):
                if input_arr[r][c+idx_r] != input_arr[r][c+M-1-idx_r]:
                    break
            else:
                print(f'#{test_case} {input_arr[r][c:c+M]}')

    for c in range(N):
        for r in range(N-M+1):
            for idx_c in range(M//2):
                if input_arr[r+idx_c][c] != input_arr[r+M-1-idx_c][c]:
                    break
            else:
                print(f'#{test_case}', end=" ")
                for idx in range(M):
                    print(input_arr[idx][c], end="")
                print()
