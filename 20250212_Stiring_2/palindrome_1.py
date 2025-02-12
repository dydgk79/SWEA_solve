T = 10
N = 8

for test_case in range(1, 1+T):
    length = int(input())
    input_arr = list(input() for _ in range(N))
    ans = 0

    for r in range(N):
        for c in range(N-length+1):
            for idx in range(length//2):
                if input_arr[r][c+idx]:
                    pass

    print(f'#{test_case} {ans}')

