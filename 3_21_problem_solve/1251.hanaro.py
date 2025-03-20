import sys
sys.stdin = open("1251.txt", "r")

from math import sqrt
from heapq import heappush, heappop


def calc_tax(idx_1, idx_2):
    l = sqrt((arr_x[idx_1]-arr_x[idx_2])**2 + (arr_y[idx_1]-arr_y[idx_2])**2)
    return E*l*l


def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * N
    min_tax = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_tax += weight

        for idx in range(N):
            if idx == node:
                continue
            if MST[idx]:
                continue
            heappush(pq, (calc_tax(idx, node), idx))
    return min_tax


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr_x = list(map(int, input().split()))
    arr_y = list(map(int, input().split()))
    E = float(input())
    print(f'#{tc} {round(prim(0))}')


