T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    ans = 0
    start = [0,0]
    end = [0,0]
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start[0] = r
                start[1] = c
            elif maze[r][c] == 3:
                end[0] = r
                end[1] = c

    i = start[0]
    j = start[1]

    delta = [[1,0], [0,1], [-1,0], [0,-1]]
    step = []
    nearby_data = [list([] for _ in range(N)) for _ in range(N)]
    visited = [list(0 for _ in range(N)) for _ in range(N)]

    while ans == 0:
        visited[i][j] = 1
        if not(nearby_data[i][j]):
            for d in delta:
                new_i = i+d[0]
                new_j = j+d[1]
                if 0<=new_i<N and 0<=new_j<N:
                    if maze[new_i][new_j] == 3:
                        ans = 1
                        break
                    elif maze[new_i][new_j] == 0:
                        nearby_data[i][j].append([new_i,new_j])
        for near_index in nearby_data[i][j]:
            if visited[near_index[0]][near_index[1]] == 0:
                step.append([i,j])
                i = near_index[0]
                j = near_index[1]
                break
        else:
            if step:
                step_data = step.pop()
                i = step_data[0]
                j = step_data[1]
            else:
                break
    print(f'#{test_case} {ans}')

