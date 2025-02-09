T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    input_list = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

    print(f'#{test_case}', end=" ")
    for idx in range(len(input_list)):
        print(f'{input_list[idx]}', end=" ")
    print()

