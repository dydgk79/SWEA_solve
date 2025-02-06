T = int(input())

for test_case in range(1, 1+T):
    input_num = list(map(int, input()))
    count_list = [0] * 12
    for idx in range(len(input_num)):
        count_list[input_num[idx]] += 1

    i = 0
    tri = 0
    runner = 0
    while i < 10:
        if count_list[i] >= 3:
            count_list[i] -= 3
            tri += 1
            continue
        if count_list[i] >= 1 and count_list[i+1] >= 1 and count_list[i+2] >= 1:
            count_list[i] -= 1
            count_list[i+1] -= 1
            count_list[i+2] -= 1
            runner += 1
            continue
        i += 1

    answer = 0
    if tri + runner == 2:
        answer = 1
    print(f'#{test_case} {answer}')
