T = int(input())

for test_case in range(1, 1+T):
    max_run, end_num, charger_num = map(int, input().split())
    charger_list = list(map(int, input().split()))

    # 충전소간 거리를 요소로 가진 배열을 만든다.
    differ = [0] * (charger_num + 1)
    for idx in range(len(charger_list)-1):
        differ[idx] = charger_list[idx+1] - charger_list[idx]
    print(differ)
    charged_num = 0

    # 그 중 하나라도 max_run 값을 넘어간다면 0을 출력
    # max_run 값과 동일하면 무조건 충전횟수 +1
    # max_run 값보다 작으면
    # 두개의 합이 max_run과 같다면 병합
    # 두개의 합이 max_run보다 작다면, 그 뒤의 것까지 확인해서 병합
    # 병합의 최대치 : 1씩 max_run만큼 있을 때. : while?
    for idx in range(len(differ)):
        if differ[idx] > max_run:
            break
        elif differ[idx] == max_run:
            charged_num += 1
            differ[idx] = 0
        else:
            sum_er = 0
            add_idx = 0
            while sum_er < max_run:
                sum_er += differ[add_idx]
                if sum_er == max_run:
                    pass
    print(differ, charged_num)
