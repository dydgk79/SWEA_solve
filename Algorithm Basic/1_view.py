T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    num_of_view = 0
    for idx in range(len(arr)):
        try:
            max_height = 0
            for num in [-2, -1, 1, 2]:
                if max_height < arr[idx+num]:
                    max_height = arr[idx+num]
            if arr[idx] > max_height:
                num_of_view += arr[idx] - max_height
        except IndexError:
            continue
    print(f'#{test_case} {num_of_view}')
