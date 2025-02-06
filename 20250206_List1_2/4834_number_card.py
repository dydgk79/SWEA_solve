T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    num_list = list(map(int, input()))

    # 각 숫자가 몇번씩 있는지 리스트에 저장한다.
    count_list = [0] * 11
    for idx in range(N):
        count_list[num_list[idx]] += 1

    # 횟수가 기존보다 크거나 같은지 비교해서 저장한다.
    maximum_num = 0
    maximum_cards = count_list[0]
    for idx in range(10):
        if maximum_cards <= count_list[idx]:
            maximum_cards = count_list[idx]
            maximum_num = idx
    print(f'#{test_case} {maximum_num} {maximum_cards}')
