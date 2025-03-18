import sys
sys.stdin = open("sample_input.txt", "r")


def recur(cnt, total):
    global min_cost
    if total >= min_cost:
        return

    if cnt == N:
        min_cost = min(min_cost,total)
        return

    for idx in range(N):
        if visited[idx]:
            continue
        visited[idx] = 1
        recur(cnt+1, total+arr[cnt][idx])
        visited[idx] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    min_cost = float('inf')
    recur(0,0)
    print(f'#{tc} {min_cost}')
