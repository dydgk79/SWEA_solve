import sys
sys.stdin = open("5251.txt", "r")

import heapq


def dij(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (N+1)
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop((pq))

        if dists[node] < dist:
            continue

        for next_info in adj[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    return dists


T = int(input())
INF = 2e18

for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((w, v))
    print(f'#{tc} {dij(0)[-1]}')

