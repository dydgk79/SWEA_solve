T = int(input())

for test_case in range(1, 1+T):
    arr = input()
    ans = 1

    checker = []
    top = -1

    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == '{':
            top += 1
            checker.append(arr[i])

        elif arr[i] == ')':
            if top == -1 or checker[top] != '(':
                ans = 0
                break
            elif checker[top] == '(':
                top -= 1
                checker.pop()

        elif arr[i] == '}':
            if top == -1 or checker[top] != '{':
                ans = 0
                break
            elif checker[top] == '{':
                top -= 1
                checker.pop()

    if top != -1:
        ans = 0

    print(f'#{test_case} {ans}')
