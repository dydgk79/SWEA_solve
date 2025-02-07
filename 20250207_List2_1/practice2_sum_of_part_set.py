T = int(input())

for test_case in range(1, 1+T):
    input_arr = list(map(int, input().split()))
    is_success = 0

    # 모든 부분집합마다 확인할 예정
    for i in range(1<<10):
        # 부분집합의 원소값을 넣을 빈 리스트 생성
        part_set = []
        for j in range(10):
            if i & (1<<j):
                part_set.append(input_arr[j])

        # 리스트의 원소들의 합의 값을 계산하고 확인하는 코드
        sum_num = 0
        for idx in range(len(part_set)):
            sum_num += part_set[idx]
            if sum_num == 0:
                is_success = 1

    print(f'#{test_case} {is_success}')
