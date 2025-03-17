import sys
sys.stdin = open("sample_input.txt", "r")


def bin_search(x, left, right, middle):
    global cnt
    global flag
    global is_in
    if x == N_list[middle]:
        is_in = True
        return
    if left == right:
        return
    if x < N_list[middle]:
        cnt += 1
        if flag == 'right':
            cnt = 2
        flag = 'left'
        bin_search(x, left, middle-1, (left + middle-1)//2)
    if x > N_list[middle]:
        cnt += 1
        if flag == 'left':
            cnt = 2
        flag = 'right'
        bin_search(x, middle+1, right, (middle+1 + right)//2)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    N_list.sort()
    ans = 0
    for idx in range(M):
        is_in = False
        flag = False
        cnt = 0
        bin_search(M_list[idx], 0, N-1, N//2)
        if cnt >= 2 or is_in:
            ans += 1
    print(f'#{tc} {ans}')
