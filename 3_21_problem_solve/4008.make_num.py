import sys
sys.stdin = open("4008.txt", "r")


def recur(cnt, total, a, m, p, d):
    global max_num, min_num
    if cnt == N:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return

    if a:
        recur(cnt + 1, total + num_arr[cnt], a-1, m, p, d)
    if m:
        recur(cnt + 1, total - num_arr[cnt], a, m-1, p, d)
    if p:
        recur(cnt + 1, total * num_arr[cnt], a, m, p-1, d)
    if d:
        if total < 0 and total%num_arr[cnt] != 0:
            recur(cnt + 1, 1 + total // num_arr[cnt], a, m, p, d - 1)
        else:
            recur(cnt + 1, total // num_arr[cnt], a, m, p, d-1)



T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    add, minus, pro, div = map(int, input().split())
    num_arr = list(map(int, input().split()))

    max_num = -float('inf')
    min_num = float('inf')
    recur(1, num_arr[0], add, minus, pro, div)
    print(f'#{tc} {max_num-min_num}')
