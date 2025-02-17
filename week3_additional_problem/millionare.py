T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    cost_list = list(map(int, input().split()))

    day = 0
    selled_day = 0
    invest = 0
    income = 0
    while day < N-1:
        if cost_list[day] <= cost_list[day+1]:
            invest += cost_list[day]
        else:
            invest += cost_list[day]
            income += (day-selled_day) * cost_list[day+1]
            selled_day = day
        day += 1
    print(income-invest)