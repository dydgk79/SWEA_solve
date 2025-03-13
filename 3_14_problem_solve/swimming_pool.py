import sys
sys.stdin = open("sample_input.txt", "r")


def recur(cnt):
    global min_pay
    if cnt == 12 or sum(path) >= 12:
        temp_sum = 0
        temp_idx = 0
        for index in path:
            if index == 1:
                temp_sum += pay[temp_idx]
                temp_idx += 1
            else:
                temp_sum += seasonal
                temp_idx += 3
        min_pay = min(temp_sum, min_pay)
        return
    for select in [1,3]:
        path.append(select)
        recur(cnt + 1)
        path.pop()


T = int(input())

for tc in range(1, T+1):
    daily, monthly, seasonal, yearly = map(int, input().split())
    plan = list(map(int, input().split()))
    pay = list([0]*12)
    for idx in range(len(plan)):
        pay[idx] = min(plan[idx]*daily, monthly)
    min_pay = yearly
    path = []

    recur(0)

    print(f'#{tc} {min_pay}')
