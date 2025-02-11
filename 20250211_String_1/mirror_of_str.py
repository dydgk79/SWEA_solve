T = int(input())

for test_case in range(1, 1+T):
    input_arr = input()
    ans = []
    n = len(input_arr)

    for idx in range(n-1, -1, -1):
        if input_arr[idx] == 'b':
            ans.append('d')
        elif input_arr[idx] == 'd':
            ans.append('b')
        elif input_arr[idx] == 'p':
            ans.append('q')
        elif input_arr[idx] == 'q':
            ans.append('p')

    print(f'#{test_case} {"".join(ans)}')