def decoder(s):
    if s == '0001101':
        return '0'
    elif s == '0011001':
        return '1'
    elif s == '0010011':
        return '2'
    elif s == '0111101':
        return '3'
    elif s == '0100011':
        return '4'
    elif s == '0110001':
        return '5'
    elif s == '0101111':
        return '6'
    elif s == '0111011':
        return '7'
    elif s == '0110111':
        return '8'
    elif s == '0001011':
        return '9'


def pwd_checker(t):
    odd = 0
    even = 0
    for num in range(1,len(t)+1):
        if num%2 == 1:
            odd += int(t[num-1])
        else:
            even += int(t[num-1])
    if (odd*3 + even) % 10 == 0:
        return odd+even
    else:
        return 0


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    code_data = [list(input().split()) for _ in range(N)]
    for r in range(N):
        if int(code_data[r][0]) == 0:
            continue
        else:
            spy_code = code_data[r][0]
            break

    password = ""
    c_idx = M-1
    while c_idx > 7:
        if spy_code[c_idx] == '1':
            code_checker = spy_code[c_idx-6:c_idx+1]
            password = decoder(code_checker) + password
            c_idx -= 7
        else:
            c_idx -= 1
    print(f'#{test_case} {pwd_checker(password)}')
