import sys
sys.stdin = open("sample_input.txt", "r")


def recur(reach, count):
    global cnt
    if count > cnt:
        return
    if reach >= N-1:
        cnt = min(count, cnt)
        return
    for idx in range(M_list[reach]):
        recur(reach+idx+1, count+1)


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    M_list = arr[1:]

    cnt = N
    recur(0,0)

    print(f'#{tc} {cnt-1}')


