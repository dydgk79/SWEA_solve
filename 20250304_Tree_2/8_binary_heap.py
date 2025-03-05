def enq(n):
    global last
    last += 1
    heap[last] = n

    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    data = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0
    for num in data:
        enq(num)
    ans = 0
    while last:
        last //= 2
        ans += heap[last]
    print(f'#{test_case} {ans}')
