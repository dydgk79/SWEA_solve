import sys
sys.stdin = open("input.txt", "r")


# n번 바꾸며 값을 찾는다.
def recur(cnt, current_money):
    global max_money

    # 손동현의 풀이 참고
    checker = (current_money, cnt)
    if checker in visited:
        return
    visited.add(checker)

    if cnt == int(change_num):
        max_money = max(max_money, int(current_money))
        return

    current_money = list(current_money)
    for i in range(n):
        for j in range(i+1, n):
            current_money[i], current_money[j] = current_money[j], current_money[i]
            recur(cnt+1, "".join(current_money))
            current_money[i], current_money[j] = current_money[j], current_money[i]


T = int(input())

for tc in range(1, 1+T):
    money, change_num = input().split()
    n = len(money)
    max_money = -float('inf')
    visited = set()
    recur(0, money)
    print(f'#{tc} {max_money}')
