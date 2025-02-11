T = int(input())

for test_case in range(1, 1+T):
    input_str = input()
    n = len(input_str)
    ans = 0
    for idx in range(n//2):
        if input_str[idx] != input_str[n-1 - idx]:
            break
    else:
        ans = 1
    print(f'#{test_case} {ans}')
