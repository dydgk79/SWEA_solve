# 2천만번
# N ~16

# 무조건 N/2개 선택
# 식재료 N 개 중 중복없이 N/2개 고르기

# 행과 열 중복 없이 N/2개 골라서 더하기, 비교하기

import sys
sys.stdin = open("4012.txt", "r")


def cook(l):
    delicious = 0
    for item_1 in l:
        for item_2 in l:
            if item_1 == item_2:
                continue
            delicious += arr[item_1][item_2]
    return delicious


def recur(cnt, start):
    global min_dif
    if cnt == N/2:
        b_set = set()
        for i in range(N):
            if i not in visited:
                b_set.add(i)
        min_dif = min(min_dif, abs(cook(visited)-cook(b_set)))
        return
    for i in range(start, N):
        if i in visited:
            continue
        visited.add(i)
        recur(cnt + 1, i+1)
        visited.remove(i)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_dif = float('inf')
    visited = set()
    recur(0, 0)
    print(f'#{tc} {min_dif}')


