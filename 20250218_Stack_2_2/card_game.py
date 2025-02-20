T = int(input())


def shobu(a, b):
    if a[1] == '1':
        if b[1] == '1' or b[1] == '3':
            return a
        else:
            return b
    elif a[1] == '2':
        if b[1] == '2' or b[1] == '1':
            return a
        else:
            return b
    else:
        if b[1] == '3' or b[1] == '2':
            return a
        else:
            return b


def tournament(a, b):
    winners = []
    if len(a) == 1 and len(b) == 1:
        parti_1 = a[0]
        parti_2 = b[0]
        winners = shobu(parti_1,parti_2)
        return winners[0]
    if len(a) == 1:
        winners.append(a[0])
    elif len(a) % 2 == 0:
        for idx in range(len(a) // 2):
            parti_1 = a[idx * 2]
            parti_2 = a[idx * 2 + 1]
            winners.append(shobu(parti_1, parti_2))
    else:
        for idx in range(len(a) // 2):
            parti_1 = a[idx * 2]
            parti_2 = a[idx * 2 + 1]
            winners.append(shobu(parti_1, parti_2))
        winners.append(a[-1])
    if len(b) == 1:
        winners.append(b[0])
    elif len(b) % 2 == 0:
        for idx in range(len(b) // 2):
            parti_1 = b[idx * 2]
            parti_2 = b[idx * 2 + 1]
            winners.append(shobu(parti_1, parti_2))
    else:
        for idx in range(len(b) // 2):
            parti_1 = b[idx * 2]
            parti_2 = b[idx * 2 + 1]
            winners.append(shobu(parti_1, parti_2))
        winners.append(b[-1])
    return winners


def team_building(i, n):
    if n%2 == 0:
        team_1 = i[0:n//2]
        team_2 = i[n//2:]
    else:
        team_1 = i[0:n//2 +1]
        team_2 = i[n//2 +1:]
    return team_1, team_2


for test_case in range(1, 1+T):
    N = int(input())
    input_arr = input().split()

    player_data = list()
    for idx in range(N):
        player_data.append([idx+1, input_arr[idx]])

    team_a, team_b = team_building(player_data, N)
    while True:
        winner = tournament(team_a, team_b)
        if type(winner) == int:
            break
        else:
            team_a, team_b = team_building(winner, len(winner))

    print(f'#{test_case} {winner}')