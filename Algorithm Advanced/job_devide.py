import sys
sys.stdin = open("sample_input.txt", "r")


def recur(cnt, product):
    global max_pro
    if product <= max_pro:
        return

    if cnt == N:
        max_pro = max(max_pro, product)
        return

    for idx in range(N):
        if visited[idx]:
            continue
        visited[idx] = 1
        recur(cnt+1, product*0.01*arr[cnt][idx])
        visited[idx] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    max_pro = -float('inf')
    recur(0,100)
    print(f'#{tc} {max_pro:.6f}')
