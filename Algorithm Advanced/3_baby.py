import sys
sys.stdin = open("input.txt", "r")


def baby(arr, cnt):
    n = len(arr)
    if cnt == 3:
        if arr[path[0]] == arr[path[1]] == arr[path[2]]:
            return True
        if arr[path[0]] == arr[path[1]]-1 == arr[path[2]]-2:
            return True
        else:
            return False
    else:
        for i in range(n):
            if i not in path:
                path.append(i)
                flag = baby(arr, cnt+1)
                if flag:
                    return True
                path.pop()


T = int(input())

for tc in range(1,T+1):
    input_arr = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    ans = 0
    for idx in range(len(input_arr)):
        if idx%2 == 0:
            player_1.append(input_arr[idx])
        else:
            player_2.append(input_arr[idx])
    for idx in range(3, 7):
        path = []
        temp_player_1 = player_1[0:idx]
        temp_n_1 = baby(temp_player_1, 0)
        if baby(temp_player_1, 0):
            ans = 1
            break
        temp_player_2 = player_2[0:idx]
        if baby(temp_player_2, 0):
            ans = 2
            break

    print(f'#{tc} {ans}')
