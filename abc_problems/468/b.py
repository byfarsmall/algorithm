M, D = map(int, input().split())
S = list(input())
guard = [0]*(M+1)

for i in range(M):
    if S[i]=='G':
        guard[max(0,i-D)] += 1
        guard[min(M-1,i+D)+1] -= 1

ruiseki = 0
ans = 0

for i in range(M):
    ruiseki += guard[i]

    if ruiseki == 0:
        ans += 1

print(ans)