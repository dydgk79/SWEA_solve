T = int(input())

for test_case in range(1, 1+T):
    winner = 0
    P, A, B = map(int, input().split())

    def binary_search(total_page, search_page):
        left, right = 1, int(total_page)
        count = 0
        while left <= right:
            c = int((left+right)/2)
            if c == search_page:
                count += 1
                return count
            elif c > search_page:
                count += 1
                right = c
            else:
                count += 1
                left = c
        return P + 1

    a_time = binary_search(P, A)
    b_time = binary_search(P, B)
    if a_time < b_time:
        winner = 'A'
    elif a_time > b_time:
        winner = 'B'

    print(f'#{test_case} {winner}')
