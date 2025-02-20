T = 10


def start_finder():
    i, j = 0, 0
    for r in range(16):
        for c in range(16):
            if maze[r][c] == '2':
                i = r
                j = c
    return i, j


for _ in range(1, 1+T):
    test_case = int(input())
    maze = [input() for _ in range(16)]
    si, sj = start_finder()
    ans = 0
    q = list()
    enqueued = [[0] * 16 for _ in range(16)]
    q.append([si, sj])
    enqueued[si][sj] = 1
    while q:
        now_i, now_j = q.pop(0)
        if maze[now_i][now_j] == '3':
            ans = 1
            break
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            new_i, new_j = now_i+di, now_j+dj
            if 0<=new_i<16 and 0<=new_j<16 and maze[new_i][new_j] != '1' and enqueued[new_i][new_j] == 0:
                q.append([new_i,new_j])
                enqueued[new_i][new_j] = 1
    print(f'#{test_case} {ans}')