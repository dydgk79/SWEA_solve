import sys
sys.stdin = open("sample_input.txt", "r")


def dive(cnt, i, j, current_sentence):
    global ans

    if cnt == 6:
        if current_sentence not in visited:
            ans += 1
            visited.add(current_sentence)
        return
    for d in delta:
        di, dj = d[0], d[1]
        ni = i + di
        nj = j + dj
        if 0<=ni<4 and 0<=nj<4:
            dive(cnt+1, ni, nj, current_sentence+input_data[ni][nj])


T = int(input())

for tc in range(1, T+1):
    input_data = [list(input().split()) for _ in range(4)]
    delta = [[1,0], [0,1], [-1,0], [0,-1]]
    ans = 0
    visited = set()
    for i in range(4):
        for j in range(4):
            dive(0, i, j, input_data[i][j])
    print(f'#{tc} {ans}')

