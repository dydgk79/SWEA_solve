T = int(input())

for test_case in range(1, 1+T):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())
    answer = 0

    # A의 부분집합을 만든다.
    for i in range(1<<12):
        list_for_sum = []
        for j in range(12):
            if i & (1<<j):
                list_for_sum.append(A[j])

        # 원소의 갯수가 N개가 아니면 넘어간다.
        if len(list_for_sum) != N:
            continue
        # 부분집합의 원소 값을 다 더하고 K와 비교하여 answer 값을 변경한다.
        else:
            sum_list = 0
            for idx in range(N):
                sum_list += list_for_sum[idx]
            if sum_list == K:
                answer += 1

    print(f'#{test_case} {answer}')
