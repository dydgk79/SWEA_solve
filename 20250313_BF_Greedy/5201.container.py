T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight_N = list(map(int, input().split()))
    weight_M = list(map(int, input().split()))
    weight_N.sort(reverse=True)
    weight_M.sort(reverse=True)
    ans = 0
    n_idx = m_idx = 0
    while weight_N and weight_M:
        if weight_M[m_idx] >= weight_N[n_idx]:
            ans += weight_N[n_idx]
            weight_N.pop(n_idx)
            weight_M.pop(m_idx)
            n_idx = m_idx = 0
        else:
            n_idx += 1
            if n_idx == len(weight_N):
                weight_M.pop(m_idx)
                n_idx = m_idx = 0
    print(f'#{tc} {ans}')


