N, M = map(int, input().split())
colors = [0]*(N+1)
events = [[] for _ in range(M + 1)]
cnt = 0

for i in range(N):
    A, D, B = map(int, input().split())
    colors[A] += 1
    events[D].append((A,B))

for x in colors:
    if x > 0:
        cnt += 1

for day in range(1, M+1):
    for A, B in events[day]:
        colors[A] -= 1

        if colors[A] == 0:
            cnt -= 1

        if colors[B] == 0:
            cnt += 1

        colors[B] += 1
    print(cnt)