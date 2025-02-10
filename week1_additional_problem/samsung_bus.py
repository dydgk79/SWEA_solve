T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    station = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for idx in range(A, B+1):
            station[idx] += 1

    print(f'#{test_case}', end=" ")
    P = int(input())
    for _ in range(P):
        print(station[int(input())], end=" ")
    print()





