T = int(input())

for test_case in range(1, 1+T):
    N, K = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 한 행에서 K칸만큼 1이 연속되었는지 확인한다.
    for i in range(N):
        for j in range(N-K+1):
            # 1이면 확인 시작
            if input_arr[i][j] == 1:
                number_count = 0
                # 첫째 열이면
                if j == 0:
                    # 현재 열에서부터 K번 확인
                    for idx in range(K):
                        if input_arr[i][j+idx] == 1:
                            number_count += 1
                        # 중간에 0이 있으면 찾는것을 멈춤
                        elif input_arr[i][j+idx] == 0:
                            break
                        # K번 1을 세었고, 그 다음이 0이면 정답값 +1
                        if number_count == K and input_arr[i][j+K] == 0:
                            ans += 1

                # 첫째 열이 아니고, 그 전의 열이 0이였다면
                elif input_arr[i][j-1] == 0:
                    for idx in range(K):
                        if input_arr[i][j+idx] == 1:
                            number_count += 1
                        else:
                            break
                        # K번 1을 세었고, 현재 열이 셀 수 있는 마지막 열이거나 다음 열의 값이 0이라면 정답값 +1
                        # j+K == N을 먼저 확인하여 인덱스에러 발생하지 않도록 함
                        if number_count == K and (j+K == N or input_arr[i][j+K] == 0):
                            ans += 1

    # 한 열에서 K칸만큼 1이 연속되었는지 확인한다.
    for j in range(N):
        for i in range(N-K+1):
            if input_arr[i][j] == 1:
                number_count = 0
                if i == 0:
                    for idx in range(K):
                        if input_arr[i+idx][j] == 1:
                            number_count += 1
                        else:
                            break
                        if number_count == K and input_arr[i+K][j] == 0:
                            ans += 1
                elif input_arr[i-1][j] == 0:
                    for idx in range(K):
                        if input_arr[i+idx][j] == 1:
                            number_count += 1
                        else:
                            break
                        if number_count == K and (i+K == N or input_arr[i+K][j] == 0):
                            ans += 1

    print(f'#{test_case} {ans}')

