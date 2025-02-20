T = int(input())


def f(i, N, s):
    # 미니멈값을 함수 안에서 변경하기 위해서 global로 선언
    global min_v

    if i == N:
        min_v = min(min_v, s)
    elif min_v < s:
        return

    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i + 1, N, s+arr[i][p[i]])
            # 원상복구
            p[i], p[j] = p[j], p[i]


for test_case in range(1,1+T):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 이 p 배열은 이따가 인덱스로 쓰일 예정
    p = [i for i in range(N)]
    min_v = float('inf')
    f(0, N, 0)
    print(f'#{test_case} {min_v}')
