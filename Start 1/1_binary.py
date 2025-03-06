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


T = int(input())

for test_case in range(1, 1+T):
    N, hex_n = input().split()
    N = int(N)
    ans = ""
    for idx in range(N):
        ans = ans + hex_to_bin(hex_n[idx])

    print(f'#{test_case} {ans}')
