T = int(input())

for test_case in range(1, 1+T):
    input_arr = list(input())
    total_sticks = 0
    n = len(input_arr)
    stick_num = 0
    ans = 0

    # input_arr 을 훑으며 레이져와 막대기를 구분하여 저장한다.
    for idx in range(n):
        # 왼쪽괄호 발견하자마자 오른쪽 괄호 오면 lr
        if input_arr[idx] == '(':
            if input_arr[idx+1] == ')':
                input_arr[idx] = 'l'
                input_arr[idx+1] = 'r'
            # 왼쪽괄호 발견하고 또 왼쪽 괄호면 중첩된 막대기 수 + 1
            elif input_arr[idx+1] == '(':
                stick_num += 1
                input_arr[idx] = stick_num
        # 오른쪽 괄호 발견했을 때, 레이져의 괄호는 이미 lr로 바뀌었으니 무조건 막대기의 괄호
        # 중첩된 막대기 수 하나 빼고 넘어감
        # 막대기 하나가 완성된 것이므로 총 막대기 수 +1
        elif input_arr[idx] == ')':
            stick_num -= 1
            input_arr[idx] = stick_num
            total_sticks += 1

    # input_arr 을 다시 훑으며 레이져가 자르는 막대기 수를 ans 에 더한다.
    # range 신경쓴다. 시작 인덱스 1, 끝 인덱스 n-1 range(1, n-1)
    # 시작과 끝에 lr이 나오는 건 의미가 없다. 1부터 시작해서 첫 l을 무시해 인덱스 에러를 무시하고
    # 왼쪽에서 자를 막대기를 찾게 해 마지막 lr은 자를 것이 0이 되도록 한다.
    for idx in range(1, n-1):
        # 숫자로 둘러쌓인 lr이 있으면, 그 옆의 숫자를 더한다.
        if input_arr[idx] == 'l':
            searching_idx = idx
            while type(input_arr[searching_idx]) is str:
                searching_idx -= 1
            ans += input_arr[searching_idx]

    # ans 는 자르면서 생긴 조각 수이다. 3조각짜리를 자르면 3조각이 생기고, 2조각짜리를 자르면 2조각이 생긴다.
    # 원래의 조각 수에 자르면서 생긴 조각 수를 더하면 총 조각수가 된다.

    print(f'#{test_case} {total_sticks + ans}')