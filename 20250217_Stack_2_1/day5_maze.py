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
            elif maze[r][c] == 0:
                pass

    i = start[0]
    j = start[1]

    d = [[1,0], [0,1], [-1,0], [0,-1]]
    direction = 0
    step = []





