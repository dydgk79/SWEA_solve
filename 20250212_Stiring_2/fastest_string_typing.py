T = int(input())

for test_case in range(1, 1+T):
    A, B = input().split()
    ans = 0
    i = 0
    count = 0

    while i < len(A) - len(B):
        for j in range(len(B)):
            if A[i+j] != B[j]:
                i += j+1
                break
        else:
            count += 1
            i += j+1

    ans = len(A) - count * (len(B) - 1)
    print(f'#{test_case} {ans}')
