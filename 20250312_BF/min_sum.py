def recur(i, j, sum):
    global min_sum
    if sum > min_sum:
        return
    if i == (N-1) and j == (N-1):
        min_sum = min(sum, min_sum)
        return
    while True:
        if 0<=i+1<N and 0<=j<N and 0<=i<N and 0<=j+1<N:
            recur(i+1, j, sum+input_arr[i+1][j])
            recur(i, j+1, sum + input_arr[i][j+1])
        elif 0 <= i+1 < N and 0 <= j < N:
            recur(i+1, j, sum + input_arr[i+1][j])
        elif 0<=i<N and 0<=j+1<N:
            recur(i, j+1, sum + input_arr[i][j+1])
        return


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    input_arr = list(list(map(int, input().split())) for _ in range(N))
    min_sum = float('inf')
    recur(0,0,input_arr[0][0])
    print(f'#{tc} {min_sum}')
