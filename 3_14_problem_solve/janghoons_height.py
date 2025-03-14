import sys
sys.stdin = open("sample_input.txt", "r")


def recur(cnt, total_sum):
    global min_height
    if total_sum >= B:
        min_height = min(min_height, total_sum)
        return
    if cnt == N:
        return
    recur(cnt+1, total_sum)
    recur(cnt+1, total_sum + height_arr[cnt])


T = int(input())

for tc in range(1, 1+T):
    N, B = map(int, input().split())
    height_arr = list(map(int, input().split()))
    min_height = float('inf')
    recur(0, 0)
    print(f'#{tc} {min_height-B}')