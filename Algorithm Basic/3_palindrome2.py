T = 10
N = 100

for _ in range(T):
    test_case = input()
    input_arr = list(input() for _ in range(N))
    ans = 0

    for r in range(N):
        for c in range(N):
            for ender in range(99,c-1,-1):
                for idx in range((ender-c)//2 + 1):
                    if input_arr[r][c+idx] != input_arr[r][ender-idx]:
                        break
                else:
                    if ans < ender - c + 1:
                        ans = ender - c + 1
                    break

    for c in range(N):
        for r in range(N):
            for ender in range(99,r-1,-1):
                for idx in range((ender-r)//2 + 1):
                    if input_arr[r+idx][c] != input_arr[ender-idx][c]:
                        break
                else:
                    if ans < ender - r + 1:
                        ans = ender - r + 1
                    break

    print(f'#{test_case} {ans}')
