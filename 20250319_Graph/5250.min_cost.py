import sys
sys.stdin = open("5250.txt", "r")

from heapq import heapify, heappop, heappush


def dij(r,c):
    pq = [(0, r, c)]
    visited = [[float('inf')]*N for _ in range(N)]
    visited[r][c] = 0

    while pq:
        fuel, i, j = heappop(pq)
        now_height = arr[i][j]
        if visited[i][j] < fuel:
            continue

        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            new_i = i+di
            new_j = j+dj
            if new_i < 0 or new_i >= N or new_j < 0 or new_j >= N:
                continue
            if arr[new_i][new_j] > now_height:
                next_fuel = fuel + 1 + arr[new_i][new_j] - now_height
            else:
                next_fuel = fuel + 1

            if visited[new_i][new_j] <= next_fuel:
                continue

            visited[new_i][new_j] = next_fuel
            heappush(pq, (next_fuel, new_i, new_j))
    return visited[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start_r = start_c = 0
    print(f'#{tc} {dij(start_r, start_c)}')