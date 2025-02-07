T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    input_arr = list(map(int, input().split()))
    min_idx = N-1
    min_value = input_arr[min_idx]
    max_idx = 0
    max_value = input_arr[max_idx]
    for idx in range(len(input_arr)):
        if min_value > input_arr[idx]:
            min_value = input_arr[idx]
            min_idx = idx
        if max_value <= input_arr[idx]:
            max_value = input_arr[idx]
            max_idx = idx
    print(f'#{test_case} {abs(max_idx - min_idx)}')
