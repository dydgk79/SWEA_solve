T = 10

for test_case in range(1, 1+T):
    t_c = input()
    N = 100
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    direction = [[1,0], [0,-1], [0,1]]
    for start_y in range(N):
        x, y = 0, start_y
        direct_num = 0

        # 시작점이 1이면 시작한다.
        if input_arr[0][y] == 1:
            # 계속 훑는다
            while x < N:
                # 움직인다
                x += direction[direct_num][0]
                y += direction[direct_num][1]

                # 가던 방향에 따라 나눈다.
                if direct_num == 1:
                    # 왼쪽으로 가던중에 왼쪽이 1이면 계속 가기로 한다.
                    if y != 0 and input_arr[x][y-1] == 1:
                        continue
                    # 왼쪽으로 가던중에 0이면 내려가기로 한다.
                    elif y != 0 and input_arr[x][y-1] == 0:
                        direct_num = 0
                    elif y == 0:
                        direct_num = 0

                elif direct_num == 2:
                    # 오른쪽으로 가던 중에 오른쪽이 1이면 계속 가기로 한다.
                    if y != N-1 and input_arr[x][y+1] == 1:
                        continue
                    # 오른쪽으로 가던 중에 0이면 내려가기로 한다.
                    elif y != N-1 and input_arr[x][y+1] == 0:
                        direct_num = 0
                    elif y == N-1:
                        direct_num = 0

                # 내려가던 중이면
                elif direct_num == 0:
                    # 도착했으면 멈춘다.
                    if x == N-1:
                        if input_arr[x][y] == 2:
                            ans = start_y
                        break
                    # 도착 못했고, 왼쪽이나 오른쪽에 1이 있으면 거기로 가기로 한다.
                    elif y != 0 and input_arr[x][y-1] == 1:
                        direct_num = 1
                    elif y != N-1 and input_arr[x][y+1] == 1:
                        direct_num = 2

    print(f'#{test_case} {ans}')
