T = int(input())

for test_case in range(1,1+T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    visited = [0]
    print(input_arr)
