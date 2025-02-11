import sys
sys.stdin = open("input_2_sum.txt", "r")

T = 10

for test_case in range(1, 1 + T):
    input_case = input()
    N = 100
    input_arr = [list(map(int, input().split())) for _ in range(N)]

    # 사용할 변수 초기화, 대각선 합은 한번씩 나오므로 여기서 선언
    max_i, max_j = -float('inf'), -float('inf')
    sum_from_0, sum_from_j = 0, 0

    for i in range(N):
        # 대각선 합을 구할 때는 i값만 있어도 되니까 여기서 계산
        sum_from_0 += input_arr[i][i]
        sum_from_j += input_arr[i][N-1-i]

        # 합으로 사용할 변수 초기화
        sum_i = 0
        sum_j = 0
        
        # 열을 순회하며 값의 합 구하기
        # NxN 행렬이므로 인덱싱 순서만 바꿔서 한번에 계산 가능
        for j in range(N):
            sum_i += input_arr[i][j]
            sum_j += input_arr[j][i]

        # 비교하여 맥스값 갱신, max(max_ij, sum_ij) 와 같은 기능
        if max_i < sum_i:
            max_i = sum_i
        if max_j < sum_j:
            max_j = sum_j

    ans = max(max_i, max_j, sum_from_0, sum_from_j)
    print(f'#{test_case} {ans}')

