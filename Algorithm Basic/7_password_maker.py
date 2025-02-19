for _ in range(10):
    tc = int(input())
    input_arr = list(map(int, input().split()))

    flag = 1
    sub = 1
    idx = 0
    while flag:
        temp = input_arr[:]
        if input_arr[0] <= sub:
            flag = 0
            break
        else:
            temp[7] = input_arr[0] - sub
            for i in range(7):
                temp[i] = input_arr[i+1]
        idx += 1
        idx %= 8
        sub += 1
        if sub == 6:
            sub = 1
        input_arr = temp
    ans = [0] * 8
    ans[7] = 0
    for i in range(7):
        ans[i] = input_arr[i + 1]

    print(f'#{tc}', end=" ")
    for idx in range(8):
        print(ans[idx], end=" ")
    print()