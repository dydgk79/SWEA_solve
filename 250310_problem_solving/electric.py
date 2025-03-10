TC = int(input())

for test_case in range(1, 1+TC):
    N = int(input())
    count = 0
    line_data = list()
    s, e = map(int, input().split())
    line_data.append([s, e])
    for _ in range(N-1):
        now_s, now_e = map(int, input().split())
        for prev_s, prev_e in line_data:
            if now_s < prev_s and now_e > prev_e:
                count += 1
            if now_s > prev_s and now_e < prev_e:
                count += 1
        line_data.append([now_s, now_e])
    print(f'#{test_case} {count}')


