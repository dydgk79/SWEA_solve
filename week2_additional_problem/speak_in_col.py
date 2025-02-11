T = int(input())

for test_case in range(1, 1+T):
    input_arr = list([0]*5 for _ in range(15))
    # 다섯줄 입력 받아 각각 저장한다.
    input_arr = list(input() for _ in range(5))

    # 각 행의 길이를 저장한다.
    len_list = [0]*5
    for i in range(5):
        len_list[i] = len(input_arr[i])

    print(f'#{test_case}', end=" ")

    compare_idx = 0
    while len_list != [0]*5:
        # 미니멈 렝스를 찾는다. 단, 0이면 안찾는다.
        min_len = float('inf')
        for i in range(5):
            if len_list[i] != 0 and len_list[i] < min_len:
                min_len = len_list[i]

        # 미니멈 행 길이만큼 정상적으로 열우선탐색, 프린트한다.
        for j in range(min_len):
            for i in range(5):
                if len_list[i] != 0:
                    print(input_arr[i][j + compare_idx], end="")

        # 행 길이 갱신한다.
        for i in range(5):
            if len_list[i] != 0:
                len_list[i] -= min_len
        compare_idx += min_len

        # len_list 가 전부 0일 때 까지 반복한다.

    print()

