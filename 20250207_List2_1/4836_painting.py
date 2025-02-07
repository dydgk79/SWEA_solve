T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    painting_arr = [[0]*10 for _ in range(10)]
    purple_count = 0

    # 색칠할 영역을 입력받고 color를 더함 (red : 1, blue : 2)
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                painting_arr[i][j] += color

    # red와 blue를 모두 칠해 3이 되면 보라색임을 확인하고 셈
    for i in range(10):
        for j in range(10):
            if painting_arr[i][j] == 3:
                purple_count += 1
    print(f'#{test_case} {purple_count}')
