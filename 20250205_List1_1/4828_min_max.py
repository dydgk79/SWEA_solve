T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_value = arr[0]
    min_value = arr[0]
    for idx in range(len(arr)):
        if arr[idx] > max_value:
            max_value = arr[idx]
        elif arr[idx] < min_value:
            min_value = arr[idx]
    print(f'#{test_case} {max_value - min_value}')
