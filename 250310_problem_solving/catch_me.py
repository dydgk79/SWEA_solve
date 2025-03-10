from collections import deque

T = int(input())

for tc in range(1, 1+T):
    N, M, R, C, L = map(int, input().split())
    map_data = [list(map(int, input().split())) for _ in range(N)]
    delta = [[-1,0], [1,0], [0,-1], [0,1]]
    tunnel_data = {
        1: [1, 1, 1, 1],
        2: [1, 1, 0, 0],
        3: [0, 0, 1, 1],
        4: [1, 0, 0, 1],
        5: [0, 1, 0, 1],
        6: [0, 1, 1, 0],
        7: [1, 0, 1, 0],
    }

    dq = deque()
    visited = [[0]*M for _ in range(N)]
    dq.append([R, C])
    visited[R][C] = 1

    while dq:
        now_r, now_c = dq.popleft()
        now_tunnel = map_data[now_r][now_c]
        for idx in range(4):
            if tunnel_data[now_tunnel][idx]:
                dr = delta[idx][0]
                dc = delta[idx][1]
                new_r = now_r+dr
                new_c = now_c+dc
                if new_r < 0 or new_r >= N:
                    continue
                if new_c < 0 or new_c >= M:
                    continue
                if visited[new_r][new_c]:
                    continue
                new_tunnel = map_data[new_r][new_c]
                if new_tunnel == 0:
                    continue
                if (idx == 0 or idx == 2) and tunnel_data[new_tunnel][idx+1] == 0:
                    continue
                if (idx == 1 or idx == 3) and tunnel_data[new_tunnel][idx-1] == 0:
                    continue
                dq.append([new_r, new_c])
                visited[new_r][new_c] = visited[now_r][now_c] + 1

    ans = 0
    for row in range(N):
        for col in range(M):
            if 0 < visited[row][col] <= L:
                ans += 1
    print(f'#{tc} {ans}')
