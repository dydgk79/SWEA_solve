T = int(input())

for test_case in range(1, 1+T):
    str1 = input()
    n = len(str1)

    str2 = input()
    m = len(str2)

    max_count = 0

    for finder in str1:
        count = 0
        for idx in range(m):
            if finder == str2[idx]:
                count += 1
        if count >= max_count:
            max_count = count

    print(f'#{test_case} {max_count}')
