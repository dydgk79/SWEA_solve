T = int(input())

for test_case in range(1, 1+T):
    input_arr = [list(map(int, input().split())) for _ in range(9)]

    # 행 9번, 열 9번, 3x3 9번 총 27번 확인할 예정
    check = 27
    ans = 0

    # 행과 열을 돌면서 1~9가 한번씩 있는지 확인
    for i in range(9):
        i_arr = [0] * 9
        for j in range(9):
            i_arr[input_arr[i][j]-1] += 1
            if i_arr == [1] * 9:
                check -= 1

    for j in range(9):
        j_arr = [0] * 9
        for i in range(9):
            j_arr[input_arr[i][j]-1] += 1
        if j_arr == [1] * 9:
            check -= 1

    # 중심좌표로부터 근처좌표를 보면서 1~9가 한번씩 있는지 확인
    center_idx = [[1, 1], [4, 1], [7, 1], [1, 4], [4, 4], [7, 4], [1, 7], [4, 7], [7, 7]]
    nearby_idx = [[-1,-1],[0,-1],[1,-1],[-1,0],[0,0],[1,0],[-1,1],[0,1],[1,1]]

    for ct_x, ct_y in center_idx:
        check_arr = [0] * 9
        for dx, dy in nearby_idx:
            check_arr[input_arr[ct_x+dx][ct_y+dy]-1] += 1
            if check_arr == [1] * 9:
                check -= 1

    if check == 0:
        ans = 1

    print(f'#{test_case} {ans}')