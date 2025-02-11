T = int(input())

for _ in range(1, 1+T):
    test_hash, N = input().split()
    N = int(N)
    input_str_list = input().split()

    converter = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for idx in range(N):
        input_str_list[idx] = converter.index(input_str_list[idx])

    input_str_list.sort()

    for idx in range(N):
        input_str_list[idx] = converter[input_str_list[idx]]

    print(f'{test_hash} {" ".join(input_str_list)}')


