T = int(input())


def node_finder(s, g):
    q = list()
    enqueued = [-1]*(V+1)
    enqueued[s] = 0
    q.append(s)
    while q:
        now = q.pop(0)
        if now == g:
            return enqueued[now]
        if node_data[now]:
            for i in node_data[now]:
                if enqueued[i] == -1:
                    q.append(i)
                    enqueued[i] = enqueued[now] + 1
    return 0


for test_case in range(1,1+T):
    V, E = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    node_data = [[] for _ in range(V+1)]
    for idx in range(E):
        x, y = input_arr[idx][0], input_arr[idx][1]
        node_data[x].append(y)
        node_data[y].append(x)
    ans = node_finder(S, G)

    print(f'#{test_case} {ans}')
