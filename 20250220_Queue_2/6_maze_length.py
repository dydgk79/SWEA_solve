T = int(input())


def starter(n):
    for r in range(n):
        for c in range(n):
            if maze[r][c] == '2':
                i, j = r, c
                return i, j


def maze_runner(s, n):
    q = list()
    visited = [[-1]*n for _ in range(n)]
    q.append(s)
    while q:
        i, j = q.pop(0)
        if maze[i][j] == '3':
            return visited[i][j]
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            new_i, new_j = i+di, j+dj
            if 0<=new_i<N and 0<=new_j<N and maze[new_i][new_j] != '1' and visited[new_i][new_j] == -1:
                q.append((new_i,new_j))
                visited[new_i][new_j] = visited[i][j] + 1
    return 0


for test_case in range(1,1+T):
    N = int(input())
    maze = [input() for _ in range(N)]
    s_idx = starter(N)
    ans = maze_runner(s_idx, N)
    print(f'#{test_case} {ans}')
