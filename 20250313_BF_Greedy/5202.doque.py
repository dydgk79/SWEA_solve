import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [[0,0] for _ in range(N)]
    for idx in range(N):
        a,b = map(int, input().split())
        data[idx] = [a,b]
    data.sort(key=lambda x:x[1])
    ans = 1
    end_time = data[0][1]

    idx = 1
    while idx < N:
        # 보는 start_time이 end_time보다 작으면 넘어간다.
        if idx < N and end_time > data[idx][0]:
            idx += 1
            continue
        # 빠르게 끝나는 회의가 확정되었다.
        # end_time을 갱신한다.
        end_time = data[idx][1]
        ans += 1
        idx += 1

    print(f'#{tc} {ans}')



