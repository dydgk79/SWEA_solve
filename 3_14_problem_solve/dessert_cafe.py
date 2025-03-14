import sys
sys.stdin = open("sample_input.txt", "r")


def recur(cnt, ni, nj, index):
    global ans
    if index == 3 and ni == i and nj == j and cnt > 2:
        ans = max(ans, cnt)
    d = delta[index]
    new_i = ni + d[0]
    new_j = nj + d[1]
    if new_i < 0 or new_i >= N or new_j < 0 or new_j >= N:
        return
    if map_data[new_i][new_j] in visited:
        return
    for idx in range(index, 4):
        visited.add(map_data[new_i][new_j])
        recur(cnt+1, new_i, new_j, idx)
        visited.remove(map_data[new_i][new_j])


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    map_data = [list(map(int, input().split())) for _ in range(N)]
    delta = [[1,1], [1,-1], [-1,-1], [-1,1]]
    ans = -1

    for i in range(N):
        for j in range(N):
            visited = set()
            recur(0, i, j, 0)

    print(f'#{tc} {ans}')
