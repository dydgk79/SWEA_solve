T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    answer = list(([0]*N) for _ in range(N))
    direction = [[0,1], [1,0], [0,-1], [-1,0]]
    x, y = 0, 0
    directing_number = 0

    for times in range(1, N*N+1):
        # 숫자 넣기
        answer[x][y] = times

        # direction 방향으로 이동
        x += direction[directing_number][0]
        y += direction[directing_number][1]

        # 이동했을 때 문제있는지 확인 (range, 0이 아닌 숫자가 들어있는가)
        # 있으면 이동 취소하고, direction 바꾸고 이동
        out_of_range = [-1, N]
        # if x == N or y == N or x == -1 or y == -1 or answer[x][y] != 0:
        if x in out_of_range or y in out_of_range or answer[x][y] != 0:
            x -= direction[directing_number][0]
            y -= direction[directing_number][1]
            directing_number += 1
            directing_number %= 4
            x += direction[directing_number][0]
            y += direction[directing_number][1]

    print(f'#{test_case}')
    for idx in range(len(answer)):
        print(*answer[idx])