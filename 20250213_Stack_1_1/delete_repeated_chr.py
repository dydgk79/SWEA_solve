T = int(input())

for test_case in range(1, 1+T):
    input_str = input()
    checker = []
    top = -1

    for item in input_str:
        if top == -1:
            checker.append(item)
            top += 1
        elif checker[top] == item:
            checker.pop()
            top -= 1
        elif checker[top] != item:
            checker.append(item)
            top += 1

    print(f'#{test_case} {len(checker)}')
