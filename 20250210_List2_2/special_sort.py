T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    input_arr = list(map(int, input().split()))

    def special_sort(a):
        length = len(a)
        for i in range(length-1):
            max_idx = i
            min_idx = i
            if i%2 == 0:
                for j in range(i+1, length):
                    if a[max_idx] < a[j]:
                        max_idx = j
                a[i], a[max_idx] = a[max_idx], a[i]
            else:
                for j in range(i+1, length):
                    if a[min_idx] > a[j]:
                        min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]


    special_sort(input_arr)
    print(f'#{test_case}', end=" ")
    for idx in range(10):
        print(f'{input_arr[idx]}', end=" ")
    print()


