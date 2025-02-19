T = int(input())

for test_case in range(1, 1+T):
    input_arr = list(input().split())
    operator = '+-*/'
    stack = [0]*256
    top = -1
    ans = 0
    for item in input_arr:
        if item in operator:
            operand2 = stack[top]
            top -= 1
            operand1 = stack[top]
            top -= 1
            if item == '+':
                top += 1
                stack[top] = operand1+operand2
            elif item == '-':
                top += 1
                stack[top] = operand1-operand2
            elif item == '*':
                top += 1
                stack[top] = operand1*operand2
            elif item == '/':
                top += 1
                stack[top] = operand1//operand2
        elif item != '.':
           top += 1
           stack[top] = int(item)
        else:
            if top != 0:
                ans = 'error'
            else:
                ans = stack[0]
    print(f'#{test_case} {ans}')
