T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    idx = M % N
    print(f'#{test_case} {num_list[idx]}')
