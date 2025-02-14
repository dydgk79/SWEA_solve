T = int(input())

for test_case in range(1, 1+T):
    V, E = map(int, input().split())
    append_list = [[] for _ in range(V+1)]

    for _ in range(E):
        v, w = map(int, input().split())
        append_list[v].append(w)

    start, end = map(int, input().split())

    ans = 1
    idx = start
    visited = [0] * (V + 1)
    stack = []
    while visited[end] != 1:
        if visited[idx] == 0:
            visited[idx] = 1

        for w in append_list[idx]:
            if visited[w] == 0:
                stack.append(w)
                idx = w
                break
        else:
            if stack:
                idx = stack.pop()
            else:
                ans = 0
                break
    print(f'#{test_case} {ans}')