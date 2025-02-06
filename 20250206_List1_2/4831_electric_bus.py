T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    station_num = list(map(int, input().split()))
    answer = 0
    counter_list = [0] * N
    for idx in range(len(station_num)):
        counter_list[station_num[idx]] = station_num[idx]
    k_idx = K

    while N > 0 and k_idx > 0:
        if N <= k_idx:
            break
        elif N-k_idx in station_num:
            answer += 1
            N -= k_idx
            k_idx = K
            continue
        elif N-k_idx not in station_num:
            k_idx -= 1
            if k_idx == 0:
                answer = 0
                break
            continue

    print(f'#{test_case} {answer}')
