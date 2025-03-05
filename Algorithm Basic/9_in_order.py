def in_order(t):
    if t:
        in_order(left[t])
        print(word[t], end="")
        in_order(right[t])


for test_case in range(1, 11):
    N = int(input())
    word = [0]*(N+1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for idx in range(1,N+1):
        input_data = list(input().split())
        word[idx] = input_data[1]
        if len(input_data) >= 3:
            left[idx] = int(input_data[2])
        if len(input_data) == 4:
            right[idx] = int(input_data[3])

    print(f'#{test_case} ', end="")
    in_order(1)
    print()
