T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            abs_sum = 0
            for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                ni = i+di
                nj = j+dj
                if 0<=ni<N:
                    abs_sum += abs(input_arr[i][j] - input_arr[ni][j])
                if 0<=nj<N:
                    abs_sum += abs(input_arr[i][j] - input_arr[i][nj])
            ans += abs_sum

    print(f'#{test_case} {ans}')
