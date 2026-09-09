N, K = map(int, input().split())
ans = 0

for a in range(1, N+1):
    for b in range(1, N+1):
        if 1<=(K-a-b)<=N:
            ans += 1

print(ans)