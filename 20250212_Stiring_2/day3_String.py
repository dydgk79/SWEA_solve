T = 10

for _ in range(1, 1+T):
    test_case = int(input())
    search_key = input()
    sentence = input()
    ans = 0
    key_len = len(search_key)

    idx = 0
    while idx <= len(sentence)-key_len:
        for key_alpha in range(key_len):
            if sentence[idx+key_alpha] != search_key[key_alpha]:
                if key_alpha == 0:
                    idx += 1
                else:
                    idx += key_alpha
                break
        else:
            ans += 1
            idx += key_len

    print(f'#{test_case} {ans}')
