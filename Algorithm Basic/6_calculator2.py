T = 10

for test_case in range(1, 1+T):
    N = int(input())
    middle_cal = input()
    digit = ['0','1','2','3','4','5','6','7','8','9']

    back_cal = ''
    operator = [0] * N
    top = -1
    # 후위표기식으로 변환
    for item in middle_cal:
        # 숫자가 들어오면 숫자 붙인다.
        if item in digit:
            back_cal += item
        # 연산이 들어오면
        else:
            # 들어있던게 없으면 나를 넣는다.
            if top == -1:
                top += 1
                operator[top] = item
            # 우선순위 높은게 들어오면 스택에 넣는다.
            elif operator[top] == '+' and item == '*':
                top += 1
                operator[top] = item
            # 우선순위 같은게 들어오면 자기를 붙인다.
            elif operator[top] == item:
                back_cal += item
            # 우선순위 낮은게 들어오면 곱하기 먼저 다 붙이고 더하기 붙인다.
            elif operator[top] == '*' and item == '+':
                while top > -1 and operator[top] == '*':
                    top -= 1
                    back_cal += '*'
                if top == -1:
                    top += 1
                    operator[top] = item
                else:
                    back_cal += item
    while top > -1:
        back_cal += operator[top]
        top -= 1

    stack = [0]*N
    top = -1
    # 후위표기식 연산
    for item in back_cal:
        # 숫자가 들어오면 스택에 저장한다.
        if item in digit:
            top += 1
            stack[top] = int(item)
        # 연산이 들어오면 스택의 두개 꺼내서 연산하고 그 값을 스택에 넣는다.
        else:
            operand_1 = stack[top]
            top -= 1
            operand_2 = stack[top]
            top -= 1
            if item == '+':
                sum = operand_1 + operand_2
                top += 1
                stack[top] = sum
            elif item == '*':
                pro = operand_1 * operand_2
                top += 1
                stack[top] = pro
    print(f'#{test_case} {stack[0]}')
