import sys
sys.stdin = open("5249.txt", "r")


def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    if ref_x == ref_y:
        return
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges.append((start, end, weight))
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(V+1)]
    cnt = 0
    result = 0

    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            result += w
            if cnt == V:
                break

    print(f'#{tc} {result}')
