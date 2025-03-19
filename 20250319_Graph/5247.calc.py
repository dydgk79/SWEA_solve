import sys
sys.stdin = open("5247.txt", "r")


def calc(x, s):
    if x == 0:
        return s+1
    elif x == 1:
        return s-1
    elif x == 2:
        return s*2
    elif x == 3:
        return s-10


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = [N]
    visited = [0] * 1000001
    visited[N] = 1
    cnt = 0
    while q and visited[M] == 0:
        new_num = q.pop(0)
        for i in range(4):
            new_calc = calc(i, new_num)
            if new_calc <= 0 or new_calc > 1000000:
                continue
            elif visited[new_calc] == 0:
                visited[new_calc] = visited[new_num] + 1
                q.append(new_calc)

    print(f'#{tc} {visited[M]-1}')

