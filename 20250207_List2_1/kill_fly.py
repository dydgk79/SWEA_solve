T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly_count = 0

    # 파리채의 (0,0) 좌표 설정
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 여기서 파리 수 초기화
            fly_count = 0
            # 그 인덱스로부터 MxM 배열의 합을 파리 수로 저장
            for k in range(0, M):
                for l in range(0, M):
                    fly_count += input_arr[i+k][j+l]
            # 기존 값과 비교하여 갱신
            max_fly_count = max(max_fly_count, fly_count)
    print(f'#{test_case} {max_fly_count}')

