def recur(s, cnt, cur_sum):
    global min_sum
    if cur_sum > min_sum:
        return
    if cnt == N and s == 0:
        min_sum = min(min_sum, cur_sum)
        return
    elif cnt == N and s != 0:
        return
    for end_idx in range(N):
        if cnt < N-1 and end_idx == 0:
            continue
        if s != end_idx and visited[end_idx] == 0:
            visited[end_idx] = 1
            path.append([s, end_idx])
            recur(end_idx, cnt + 1, cur_sum + input_arr[s][end_idx])
            visited[end_idx] = 0
            path.pop()


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    input_arr = list(list(map(int, input().split())) for _ in range(N))
    path = []
    visited = [0]*N
    min_sum = float('inf')
    recur(0, 0, input_arr[0][0])
    print(f'#{tc} {min_sum}')
