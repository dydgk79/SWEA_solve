def post_order(idx):
    global calc
    if node[idx]:
        post_order(left[idx])
        post_order(right[idx])
        if type(node[idx]) == str:
            num2 = calc.pop()
            num1 = calc.pop()
            if node[idx] == '+':
                calc.append(num1+num2)
            elif node[idx] == '-':
                calc.append(num1-num2)
            elif node[idx] == '*':
                calc.append(num1*num2)
            elif node[idx] == '/':
                calc.append(num1//num2)
        else:
            calc.append(node[idx])


for test_case in range(1, 11):
    N = int(input())
    node = [0]*(N+1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    calc = []
    for _ in range(N):
        input_data = list(input().split())
        index = int(input_data[0])
        if input_data[1] in '+-*/':
            node[index] = input_data[1]
            left[index] = int(input_data[2])
            right[index] = int(input_data[3])
        else:
            node[index] = int(input_data[1])
    post_order(1)
    print(f'#{test_case} {calc[0]}')
