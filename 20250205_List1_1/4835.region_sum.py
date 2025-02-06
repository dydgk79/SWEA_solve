T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_value = 0
    min_value = N*10000
    for idx in range(len(arr)):
        try:
            sum_of_idx = 0
            for idx_2 in range(M):
                sum_of_idx += arr[idx+idx_2]
            if max_value < sum_of_idx:
                max_value = sum_of_idx
            if min_value > sum_of_idx:
                min_value = sum_of_idx
        except IndexError:
            continue

    print(f'#{test_case} {max_value-min_value}')

