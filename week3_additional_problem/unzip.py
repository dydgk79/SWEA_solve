T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    answer_list = []
    for _ in range(N):
        alpha, num = input().split()
        num = int(num)
        for _ in range(num):
            answer_list.append(alpha)

    print(f'#{test_case}')
    while answer_list:
        for idx in range(10):
            if answer_list:
                print(answer_list.pop(0), end="")
            else:
                break
        print()
