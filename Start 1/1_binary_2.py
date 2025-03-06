T = int(input())

for test_case in range(1, 1+T):
    N = float(input())
    pow = -1
    ans = 'overflow'
    temp_ans = ""
    while pow >= -13:
        if N == 0:
            ans = temp_ans
            break
        if 2**pow <= N:
            N -= 2**pow
            temp_ans = temp_ans + '1'
            pow -= 1
        else:
            temp_ans = temp_ans + '0'
            pow -= 1
    print(f'#{test_case} {ans}')
