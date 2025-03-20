import sys
sys.stdin = open("1249.txt", "r")

from heapq import heappop, heappush

def dij(r,c):
    pq = [(0, r, c)]
    visited = [[float('inf')]*N for _ in range(N)]
    visited[r][c] = 0

    while pq:
        time_cnt, i, j = heappop(pq)
        if visited[i][j] < time_cnt:
            continue

        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            new_i = i+di
            new_j = j+dj
            if new_i < 0 or new_i >= N or new_j < 0 or new_j >= N:
                continue

            time_cnt = arr[new_i][new_j] + visited[i][j]

            if visited[new_i][new_j] <= time_cnt:
                continue

            visited[new_i][new_j] = time_cnt
            heappush(pq, (time_cnt, new_i, new_j))
    return visited[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start_r = start_c = 0
    print(f'#{tc} {dij(start_r, start_c)}')

