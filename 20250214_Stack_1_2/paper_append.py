T = int(input())

for test_case in range(1, 1+T):
    N = int(input()) // 10
    paper = [0] * 31
    paper[1] = 1
    idx = 2

    # N이 홀수이면 직전 수에서 *2 - 1
    # 직전의 그림에서 양 옆에 얇은 막대기 하나씩 붙인다고 생각
    # 전부 얇은 막대기면 중복이니까 하나 빼기

    # N이 짝수이면 직전 수에서 *2 - 1 + 2
    # 새로 생기는 경우의 수인, 가로 20짜리로만 이루어지는 경우

    while paper[N] == 0:
        if idx % 2 == 0:
            paper[idx] = paper[idx - 1] * 2 +1
            idx += 1
        else:
            paper[idx] = paper[idx - 1] * 2 -1
            idx += 1
    print(f'#{test_case} {paper[N]}')