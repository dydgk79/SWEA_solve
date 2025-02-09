T = int(input())

for test_case in range(1, 1+T):
    N, K = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 한 행에서 K칸 이상 1이 연속되었는지 확인한다.
    for i in range(N):
        for j in range(N-K):
            if input_arr[i][j] == 1:
                check_count = 1
                for check_idx in range(K):
                    if input_arr[i][j+check_idx] == 1 and check_count != K:
                        check_count += 1
                    elif input_arr[i][j+check_idx] == 1 and check_count == K:
                        if j+check_idx+1 == N or input_arr[i][j+check_idx+1] == 0:
                            ans += 1
                            break
                        # else:
                        #     break
                    else:
                        break




    # 한 열에서 K칸 이상 1이 연속되었는지 확인한다.
    for j in range(N):
        for i in range(N-K):
            if input_arr[i][j] == 1:
                check_count = 1
                for check_idx in range(K):
                    if input_arr[i+check_idx][j] == 1 and check_count != K:
                        check_count += 1
                    elif input_arr[i+check_idx][j] == 1 and check_count == K:
                        if i+check_idx+1 == N or input_arr[i+check_idx+1][j] == 0:
                            ans += 1
                            break
                        # else:
                        #     break
                    else:
                        break



    print(f'{test_case} {ans}')

