import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check_arr = [0]*(N*N+1)
    delta = [[1,0], [0,1], [-1,0], [0,-1]]

    for i in range(N):
        for j in range(N):
            for d in delta:
                ni = i+d[0]
                nj = j+d[1]
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] == arr[i][j]+1:
                        check_arr[arr[i][j]] = 1

    s_idx = max_cnt = cnt = 0
    for idx in range(N*N+1):
        if check_arr[idx] == 1:
            cnt += 1
        if check_arr[idx] == 0:
            if max_cnt < cnt:
                max_cnt = cnt
                s_idx = idx-cnt
            cnt = 0
    print(f'#{tc} {s_idx} {max_cnt+1}')


