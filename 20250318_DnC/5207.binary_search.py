def bin_search(l, r, m):
    global ans
    global is_in
    global flag
    global cnt
    if l > r:
        return -1
    if N_list[m] == M_list[idx]:
        is_in = True
        cnt = 2
        return True
    elif M_list[idx] < N_list[m]:
        if flag == 'left':
            flag = False
            cnt = 0
            return
        cnt += 1
        flag = 'left'
        return bin_search(l, m-1, (l+m-1)//2)
    elif M_list[idx] > N_list[m]:
        if flag == 'right':
            flag = False
            cnt = 0
            return
        cnt += 1
        flag = 'right'
        return bin_search(m+1, r, (m+1+r)//2)


T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_list.sort()
    M_list = list(map(int, input().split()))

    ans = 0
    left = 0
    right = N - 1
    middle = (left + right) // 2
    for idx in range(len(M_list)):
        is_in = False
        flag = False
        cnt = 0
        bin_search(left, right, middle)
        if cnt >= 2 and is_in:
            ans += 1
    print(f'#{tc} {ans}')

"""
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5

"""