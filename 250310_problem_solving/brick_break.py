import sys
sys.stdin = open("input.txt", "r")

import copy
from collections import deque


def shot(arr, j, r):
    temp_arr = copy.deepcopy(arr)
    remain_cnt = r
    for r in range(H):
        if temp_arr[r][j]:
            top = r
            break
    else:
        return temp_arr, remain_cnt
    sr, se = top, j
    dq = deque([])
    visited = [[0]*W for _ in range(H)]
    dq.append([sr, se])
    visited[sr][se] = 1
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while dq:
        now_r, now_c = dq.popleft()
        bomb_num = arr[now_r][now_c]
        temp_arr[now_r][now_c] = 0
        remain_cnt -= 1
        for d in delta:
            for k in range(1,bomb_num):
                new_r = now_r + k*d[0]
                new_c = now_c + k*d[1]
                if new_r < 0 or new_r >= H:
                    continue
                if new_c < 0 or new_c >= W:
                    continue
                if visited[new_r][new_c]:
                    continue
                if arr[now_r][now_c] == 0:
                    continue
                dq.append([new_r, new_c])
                visited[new_r][new_c] = 1
    return temp_arr, remain_cnt


def downer(arr):
    temp_arr = copy.deepcopy(arr)
    for c in range(W):
        height = H-1
        for idx in range(height-1, -1, -1):
            if temp_arr[height][c]:
                break
            elif temp_arr[height][c] == 0 and temp_arr[idx][c]:
                temp_arr[height][c], temp_arr[idx][c] = temp_arr[idx][c], temp_arr[height][c]
    return temp_arr


T = int(input())

for tc in range(1):
    N, W, H = map(int, input().split())
    brick_data = [list(map(int, input().split())) for _ in range(H)]
    min_value = float('inf')
    remain = 0
    for r in range(H):
        for c in range(W):
            if brick_data[r][c]:
                remain += 1
    brick_data, remain = shot(brick_data, 9, remain)
    brick_data, remain = shot(brick_data, 9, remain)
    brick_data = downer(brick_data)
    print(brick_data)
