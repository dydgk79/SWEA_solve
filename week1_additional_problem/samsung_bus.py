T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    station = [0] * 5001
    station_output = [0] * 5001
    for _ in range(N):
        A, B = map(int,input().split())
        for idx in range(A, B+1):
            station[idx] += 1
    P = int(input())
    count_c = 0
    for _ in range(P):
        C = int(input())
        station_output[C] += 1
        count_c += 1
    print(f'#{test_case}', end=" ")
    for idx in range(5001):
        if station_output[idx] and count_c != 1:
            print(f'{station[idx]}', end=" ")
            count_c -= 1
        elif station_output[idx]:
            print(f'{station[idx]}')


