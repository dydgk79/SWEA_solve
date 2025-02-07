T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    input_arr = list(map(int, input()))
    max_one = 0

    # 인픗으로 들어온 리스트를 순회한다.
    for idx in range(len(input_arr)):
        num_of_one = 0
        # 리스트의 값이 1이면 코드 시작
        # 그 순간의 인덱스로부터 뒤까지 얼마나 1이 연속한지 확인한다.
        if input_arr[idx] == 1:
            temp_idx = idx
            num_of_one += 1
            # 앞에서부터 and 를 판별하므로 인덱스에러도 뜨지 않는다.
            # 지금 인덱스가 끝이거나, 다음에 오는 값이 0이 오면 while 끝
            while temp_idx < N-1 and input_arr[temp_idx+1] == 1:
                temp_idx += 1
                num_of_one += 1
            # 그 값이 기존의 값보다 크면 갱신
            max_one = max(max_one, num_of_one)
    print(f'#{test_case} {max_one}')
