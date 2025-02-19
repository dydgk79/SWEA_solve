T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    input_arr = list(map(int, input().split()))
    pizza_list = []
    # 피자의 번호와 치즈의 양을 하나의 리스트로 표현한다.
    for idx in range(M):
        pizza_list.append([idx,input_arr[idx]])

    oven = [0] * N

    idx = -1
    pizza_index = 0
    while True:
        idx += 1
        idx %= N
        if oven[idx] == 0:
            oven[idx] = pizza_list[pizza_index]
            pizza_index += 1
        else:
            oven[idx][1] //= 2
            if oven[idx][1] == 0:
                oven[idx] = pizza_list[pizza_index]
                pizza_index += 1
        if pizza_index == M:
            break
    ans = 0
    while True:
        idx += 1
        idx %= N
        if oven[idx] == 0:
            continue
        else:
            oven[idx][1] //= 2
            if oven[idx][1] == 0:
                ans = oven[idx][0]
                oven[idx] = 0
        if oven == [0] * N:
            break
    print(f'#{test_case} {ans+1}')
