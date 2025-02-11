T = int(input())

for test_case in range(1, 1+T):
    str1 = input()
    n = len(str1)
    str2 = input()
    m = len(str2)

    ans = 0

    for i in range(m-n+1):
        for j in range(n):
            if str1[j] != str2[i + j]:
                break
        else:
            ans += 1

    print(f'#{test_case} {ans}')
