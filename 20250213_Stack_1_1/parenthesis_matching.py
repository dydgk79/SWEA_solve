T = 10

for test_case in range(1, 1+T):
    N = int(input())
    input_arr = input()
    ans = 1

    checker = []
    top = -1

    for item in input_arr:
        if item in ['(', '[', '{', '<']:
            checker.append(item)
            top += 1
        elif top == -1:
            ans = 0
            break
        elif item == ')':
            if checker[top] != '(':
                ans = 0
                break
            else:
                checker.pop()
                top -= 1
        elif item == ']':
            if checker[top] != '[':
                ans = 0
                break
            else:
                checker.pop()
                top -= 1
        elif item == '}':
            if checker[top] != '{':
                ans = 0
                break
            else:
                checker.pop()
                top -= 1
        elif item == '>':
            if checker[top] != '<':
                ans = 0
                break
            else:
                checker.pop()
                top -= 1

    if checker:
        ans = 0
    print(f'#{test_case} {ans}')
