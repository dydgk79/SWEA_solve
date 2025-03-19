import sys
sys.stdin = open("5248.txt", "r")


def make_set(n):
    parents = [i for i in range(n+1)]
    return parents


def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    if ref_x == ref_y:
        return
    if ref_x < ref_y:
        parent[ref_y] = ref_x
    else:
        parent[ref_x] = ref_y


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = make_set(N)

    for idx in range(M):
        s, e = arr[idx*2], arr[idx*2+1]
        union(s, e)

    for idx in range(1, 1+N):
        find_set()

    set_num = set()
    for idx in range(1, 1+N):
        if parent[idx] not in set_num:
            set_num.add(parent[idx])

    print(f'#{tc} {len(set_num)}')
