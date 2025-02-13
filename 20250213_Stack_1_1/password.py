T = 10

for test_case in range(1, 1+T):
    N, input_arr = input().split()
    N = int(N)
    checker = []
    top = -1

    for idx in range(N):
        if top == -1:
            checker.append(input_arr[idx])
            top += 1
        elif checker[top] == input_arr[idx]:
            checker.pop()
            top -= 1
        elif checker[top] != input_arr[idx]:
            checker.append(input_arr[idx])
            top += 1
    print(f'#{test_case} {"".join(checker)}')
