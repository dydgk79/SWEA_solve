def recur(cnt, total_sum):
    global ans
    if total_sum > K:
        return
    if total_sum == K:
        ans += 1
        return
    if cnt == len(arr):
        return
    recur(cnt+1, total_sum+arr[cnt])
    recur(cnt+1, total_sum)


T = int(input())

for tc in range(1, 1+T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    recur(0, 0)
    print(f'#{tc} {ans}')
