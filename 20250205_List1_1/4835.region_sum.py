T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_value = 0
    min_value = 0
    for idx in range(len(arr)-M):
        sum_of_idx = 0
        sum_try = M
        while sum_try > 1:
            sum_of_idx += arr[idx-sum_try]
            sum_try -= 1
        if min_value == 0:
            min_value = sum_of_idx
        if max_value < sum_of_idx:
            max_value = sum_of_idx
        elif min_value > sum_of_idx:
            min_value = sum_of_idx

    print(f'#{test_case} {max_value-min_value}')
