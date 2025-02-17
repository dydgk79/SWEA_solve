T = 10

for test_case in range(1, 1+T):
    N = int(input())
    middle_cal = input()
    calculator = []

    back_cal = []

    # 후위표기식으로 변환
    for idx in range(N):
        # 연산이 들어오면 저장한다.
        if middle_cal[idx] == '+':
            calculator.append('+')
        # 숫자가 들어오면 숫자 붙이고, 연산 붙이고, 연산 없앤다.
        else:
            if idx != 0:
                back_cal.append(int(middle_cal[idx]))
                back_cal.append(calculator.pop())
            else:
                back_cal.append(int(middle_cal[0]))

    digit = []

    # 후위표기식 연산
    for idx in range(N):
        # 숫자가 들어오면 스택에 저장한다.
        if back_cal[idx] != '+':
            digit.append(back_cal[idx])
        # 연산이 들어오면 스택의 두개 꺼내서 연산하고 그 값을 스택에 넣는다.
        else:
            num1 = digit.pop()
            num2 = digit.pop()
            sum = num1 + num2
            digit.append(sum)

    print(f'#{test_case} {digit[0]}')
