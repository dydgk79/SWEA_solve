def hex_to_bin(s):
    if s == '0':
        return '0000'
    elif s == '1':
        return '0001'
    elif s == '2':
        return '0010'
    elif s == '3':
        return '0011'
    elif s == '4':
        return '0100'
    elif s == '5':
        return '0101'
    elif s == '6':
        return '0110'
    elif s == '7':
        return '0111'
    elif s == '8':
        return '1000'
    elif s == '9':
        return '1001'
    elif s == 'A':
        return '1010'
    elif s == 'B':
        return '1011'
    elif s == 'C':
        return '1100'
    elif s == 'D':
        return '1101'
    elif s == 'E':
        return '1110'
    elif s == 'F':
        return '1111'


def decoder(a, b, c, k):
    if a//k == 2 and b//k == 1 and c//k == 1:
        return '0'
    elif a//k == 2 and b//k == 2 and c//k == 1:
        return '1'
    elif a//k == 1 and b//k == 2 and c//k == 2:
        return '2'
    elif a//k == 4 and b//k == 1 and c//k == 1:
        return '3'
    elif a//k == 1 and b//k == 3 and c//k == 2:
        return '4'
    elif a//k == 2 and b//k == 3 and c//k == 1:
        return '5'
    elif a//k == 1 and b//k == 1 and c//k == 4:
        return '6'
    elif a//k == 3 and b//k == 1 and c//k == 2:
        return '7'
    elif a//k == 2 and b//k == 1 and c//k == 3:
        return '8'
    elif a//k == 1 and b//k == 1 and c//k == 2:
        return '9'


def pwd_checker(s):
    odd = 0
    even = 0
    for num in range(1,8):
        if num%2 == 1:
            odd += int(s[num-1])
        else:
            even += int(s[num-1])
    if (odd*3 + even + int(s[-1])) % 10 == 0:
        return odd+even+int(s[-1])
    else:
        return 0


def code_finder(use_idx):
    ratio_1 = ratio_2 = ratio_3 = 0
    now_num = '1'
    while True:
        if spy_code[use_idx] == now_num:
            ratio_3 += 1
            use_idx -= 1
            continue
        else:
            ratio_2 += 1
            use_idx -= 1
            now_num = '0'
            while True:
                if spy_code[use_idx] == now_num:
                    ratio_2 += 1
                    use_idx -= 1
                else:
                    ratio_1 += 1
                    use_idx -= 1
                    now_num = '1'
                    while True:
                        if spy_code[use_idx] == now_num:
                            ratio_1 += 1
                            use_idx -= 1
                        else:
                            return [ratio_1, ratio_2, ratio_3]


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    code_data = [list(input().split()) for _ in range(N)]
    spy_codes = list()
    for r in range(N):
        if code_data[r][0] == '0'*M:
            continue
        else:
            if code_data[r][0] in spy_codes:
                continue
            else:
                spy_codes.append(code_data[r][0])

    for idx in range(len(spy_codes)):
        converted = ""
        for c in spy_codes[idx]:
            converted = converted + hex_to_bin(c)
        spy_codes[idx] = converted
        spy_codes[idx] = spy_codes[idx].rstrip('0')
    passwords = set()
    for spy_code in spy_codes:
        password = ""
        use_idx = len(spy_code) - 1
        while use_idx > 8:
            if spy_code[use_idx] == '1':
                [a, b, c] = code_finder(use_idx)
                k = min(a, b, c)
                password = decoder(a, b, c, k) + password
                use_idx -= 7*k
            else:
                use_idx -= 1
        if len(password)%8:
            while len(password)%8:
                password = '0' + password
        passwords.add(password)

    eight_bits_pwd = set()
    for pwd in passwords:
        for idx in range(len(pwd)//8):
            eight_bits_pwd.add(pwd[idx*8:idx*8+8])
    ans = 0
    for item in eight_bits_pwd:
        ans += pwd_checker(item)
    print(f'#{test_case} {ans}')
