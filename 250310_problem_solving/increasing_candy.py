T = int(input())

for tc in range(1, 1+T):
    A, B, C = map(int, input().split())
    ans = 0
    if B < 2 or C < 3:
        ans = -1
    else:
        if B >= C:
            ans += B - (C - 1)
            B = C - 1
        if A >= B:
            ans += A - (B - 1)
    print(f'#{tc} {ans}')
