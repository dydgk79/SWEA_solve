T = 10
N = 8

for test_case in range(1, 1+T):
    length = int(input())
    input_arr = list(input() for _ in range(N))
    ans = 0

    for r in range(N):
        for c in range(N-length+1):
            for idx in range(length//2):
                if input_arr[r][c+idx] != input_arr[r][c+length-1-idx]:
                    break
            else:
                ans += 1

    for c in range(N):
        for r in range(N-length+1):
            for idx in range(length//2):
                if input_arr[r+idx][c] != input_arr[r+length-1-idx][c]:
                    break
            else:
                ans += 1

    print(f'#{test_case} {ans}')

