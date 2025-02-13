T = int(input())

for t in range(1, 1+T):
    N = int(input())
    ans_list = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j == 0 or j == i:
                ans_list[i][j] = 1
            elif 0 < j < i :
                ans_list[i][j] = ans_list[i-1][j-1] + ans_list[i-1][j]

    print(f'#{t}')

    for i in range(N):
        for j in range(N):
            if ans_list[i][j] != 0:
                print(ans_list[i][j], end=" ")
            else:
                print()
                break
    print()