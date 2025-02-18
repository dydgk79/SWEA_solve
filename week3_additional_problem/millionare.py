T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    input_arr = list(map(int, input().split()))
    cost_stack = []
    day = 0
    invest = 0

    # 최고가와 날짜값을 스택에 넣는 과정
    for idx in range(N):
        day += 1
        temp_data = [input_arr[idx], day]
        compare_pointer = len(cost_stack)-1
        while cost_stack and cost_stack[compare_pointer][0] < temp_data[0]:
            cost_stack.pop()
            compare_pointer -= 1
        cost_stack.append(temp_data)
        invest += input_arr[idx]

    # 정산
    income = 0
    if cost_stack:
        selled_day = 0
        for item in cost_stack:
            income += item[0]*(item[1]-selled_day)
            selled_day = item[1]

    print(f'#{test_case} {income-invest}')
