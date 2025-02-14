T = 10


def road_finder(list):
    visited = [0] * 100
    stack = []
    v = 0
    while visited[99] != 1:
        if visited[v] == 0:
            visited[v] = 1
        for w in list[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return 0
    return 1


for _ in range(1, 1+T):
    arr1 = [0] * 100
    arr2 = [0] * 100
    test_case, num_of_road = map(int, input().split())
    road_data = list(map(int,input().split()))
    adj_list = [[] for _ in range(100)]
    for i in range(num_of_road):
        v, w = road_data[i * 2], road_data[i * 2 + 1]

        adj_list[v].append(w)

    print(f'#{test_case} {road_finder(adj_list)}')